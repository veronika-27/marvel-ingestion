import os
from pathlib import Path
from metadata import Metadata
from marvelapi import MarvelAPI
from marvel_characters import MarvelCharacters
from marvel_comics import MarvelComics
from marvel_creators import MarvelCreators
from marvel_events import MarvelEvents
from marvel_series import MarvelSeries
from marvel_stories import MarvelStories
from sf.sf_setup import SqlExecution
from aws.aws_bucket import AWSBuckets
from aws.aws_roles_and_policies import AWSRolesAndPolicies


def create_initial_setup():
    bucket_name = os.environ.get("BUCKET_NAME")
    bucket_region = os.environ.get("BUCKET_REGION")

    # create bucket
    my_bucket = AWSBuckets()
    my_bucket.create_bucket(bucket_name, region=bucket_region)
    # create policy
    my_policies = AWSRolesAndPolicies()
    my_policies.create_bucket_policy(policy_name=bucket_name + "-s3-full")
    # create role
    my_policies.create_s3_role("S3_access_role", account=os.environ.get("SF_IAM_ID"))
    # list policies
    arn_policy = my_policies.list_policies(bucket_name + "-s3-full")
    # attache policy to role
    my_policies.attach_policy_to_role("S3_access_role", arn_policy)
    # SF S3 setup
    my_policies.create_sf_read_only_policy(
        resource="arn:aws:s3:::" + bucket_name + "/ingest_data/*",
        policy_name=bucket_name + "-snowflake-read-only",
        bucket_name=bucket_name,
    )
    my_policies.create_sf_role(
        aws=os.environ.get("STORAGE_AWS_IAM_USER_ARN"),
        external_id=os.environ.get("STORAGE_AWS_EXTERNAL_ID"),
        role_name=bucket_name + "-SF",
    )
    arn_sf_policy = my_policies.list_policies(
        policy_name=bucket_name + "-snowflake-read-only"
    )
    my_policies.attach_policy_to_role(bucket_name + "-SF", arn_sf_policy)

    Metadata.data["initial_setup"] = "completed"


def s3_upload():
    my_bucket = AWSBuckets()
    my_bucket.create_folder(os.environ.get("BUCKET_NAME"), "ingest_data")
    files_list = [
        file for file in os.listdir("./") if os.path.isfile(os.path.join("./", file))
    ]

    for file in files_list:
        my_bucket.upload_file_to_folder(
            "{file_name}".format(file_name=file),
            os.environ.get("BUCKET_NAME"),
            "ingest_data/{file_name}".format(file_name=file),
        )
    print("S3 upload completed!")


def s3_download():
    my_bucket = AWSBuckets()
    try:
        my_bucket.download_s3_folder(
            bucket_name=os.environ.get("BUCKET_NAME"),
            s3_folder="ingest_data",
            local_dir="./",
        )
    except:
        print("Can not download the S3 bucket to the local folder")


def switch_state():
    if Metadata.data.get("state") == "initial":
        Metadata.data["state"] = "incremental"

    # remove local and s3 csvs
    my_bucket = AWSBuckets()
    my_bucket.remove_csvs(bucket_name=os.environ.get("BUCKET_NAME"))
    files_list = [
        file for file in os.listdir("./") if os.path.isfile(os.path.join("./", file))
    ]
    for file in files_list:
        if file.endswith(".csv"):
            try:
                os.remove(file)
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))

    MarvelCharacters.initial_metadata("incremental")
    MarvelComics.initial_metadata("incremental")
    MarvelCreators.initial_metadata("incremental")
    MarvelEvents.initial_metadata("incremental")
    MarvelSeries.initial_metadata("incremental")
    MarvelStories.initial_metadata("incremental")


def process_snowflake():
    sf_obj = SqlExecution(
        sf_account=os.environ.get("SF_ACCOUNT"),
        sf_username=os.environ.get("SF_USERNAME"),
        sf_password=os.environ.get("SF_PASSWORD"),
        sf_warehouse=os.environ.get("SF_WAREHOUSE"),
        sf_database=os.environ.get("SF_DATABASE"),
        sf_role=os.environ.get("SF_ROLE"),
        sf_schema=os.environ.get("SF_SCHEMA"),
        sf_iam_id=os.environ.get("SF_IAM_ID"),
        bucket_name=os.environ.get("BUCKET_NAME"),
    )

    sf_obj.sf_s3_initial_setup()

    if Metadata.data.get("state") == "initial":
        sf_obj.copy_data_into_sf(table_name="characters")
        sf_obj.copy_data_into_sf(table_name="rel_characters_comics")
        sf_obj.copy_data_into_sf(table_name="rel_characters_events")
        sf_obj.copy_data_into_sf(table_name="comics")
        sf_obj.copy_data_into_sf(table_name="creators")
        sf_obj.copy_data_into_sf(table_name="rel_creators_comics")
        sf_obj.copy_data_into_sf(table_name="events")
        sf_obj.copy_data_into_sf(table_name="stories")
        sf_obj.copy_data_into_sf(table_name="series")
    else:
        sf_obj.truncate_sf_table(table_name="characters_incr")
        sf_obj.copy_data_into_sf(table_name="characters_incr", csv_name="characters")

        sf_obj.truncate_sf_table(table_name="rel_characters_comics_incr")
        sf_obj.copy_data_into_sf(
            table_name="rel_characters_comics_incr", csv_name="rel_characters_comics"
        )

        sf_obj.truncate_sf_table(table_name="rel_characters_events_incr")
        sf_obj.copy_data_into_sf(
            table_name="rel_characters_events_incr", csv_name="rel_characters_events"
        )

        sf_obj.truncate_sf_table(table_name="comics_incr")
        sf_obj.copy_data_into_sf(table_name="comics_incr", csv_name="comics")

        sf_obj.truncate_sf_table(table_name="creators_incr")
        sf_obj.copy_data_into_sf(table_name="creators_incr", csv_name="creators")

        sf_obj.truncate_sf_table(table_name="rel_creators_comics_incr")
        sf_obj.copy_data_into_sf(
            table_name="rel_creators_comics_incr", csv_name="rel_creators_comics"
        )

        sf_obj.truncate_sf_table(table_name="events_incr")
        sf_obj.copy_data_into_sf(table_name="events_incr", csv_name="events")

        sf_obj.truncate_sf_table(table_name="stories_incr")
        sf_obj.copy_data_into_sf(table_name="stories_incr", csv_name="stories")

        sf_obj.truncate_sf_table(table_name="series_incr")
        sf_obj.copy_data_into_sf(table_name="series_incr", csv_name="series")

        sf_obj.sf_tables_merge()

    print("SF part completed!")


def ingest_data():
    if "state" not in Metadata.data:
        Metadata.data["state"] = "initial"

    marvelAPI = MarvelAPI(
        public_key=os.environ.get("API_PUBLIC_KEY"),
        private_key=os.environ.get("API_PRIVATE_KEY"),
    )

    print("Ingesting Characters...")
    marvelCharacters = MarvelCharacters(marvelAPI=marvelAPI)
    marvelCharacters.ingest()

    print("Ingesting Comics...")
    marvelComics = MarvelComics(marvelAPI=marvelAPI)
    marvelComics.ingest()

    print("Ingesting Creators...")
    marvelCreators = MarvelCreators(marvelAPI=marvelAPI)
    marvelCreators.ingest()

    print("Ingesting Events...")
    marvelEvents = MarvelEvents(marvelAPI=marvelAPI)
    marvelEvents.ingest()

    print("Ingesting Series...")
    marvelSeries = MarvelSeries(marvelAPI=marvelAPI)
    marvelSeries.ingest()

    print("Ingesting Stories...")
    marvelStories = MarvelStories(marvelAPI=marvelAPI)
    marvelStories.ingest()


def env_vars_check():
    if os.environ.get("API_PUBLIC_KEY") is None:
        raise ("API_PUBLIC_KEY ENVIRONMENT variable is not set")

    if os.environ.get("API_PRIVATE_KEY") is None:
        raise ("API_PRIVATE_KEY ENVIRONMENT variable is not set")


def marvel_ingestion_pipeline():
    # change the CWD to be our base path
    source_path = Path(__file__).resolve()
    base_dir = source_path.parent.parent
    ing_path = str(base_dir) + "/ingest_data"
    try:
        os.mkdir(ing_path)
    except:
        pass
    os.chdir(ing_path)

    s3_download()

    # loading the metadata
    metadata = Metadata()
    metadata.load()

    if not Metadata.data:
        try:
            create_initial_setup()
        except:
            print("The initial setup has failed, probably is already completed")

    try:
        print("About to Ingest Data...")
        ingest_data()
        print("Ingest data finished, about to upload to S3...")
        s3_upload()
        print("S3 Upload has finished, about to process to snowflake...")
        process_snowflake()
        print("SnowFlake data processing has finished, switching the state...")
        switch_state()
    finally:
        print("Finally saving the latest metadata")
        metadata.save()
        print("Uploading the latest metadata to S3")
        s3_upload()


if __name__ == "__main__":
    env_vars_check()
    marvel_ingestion_pipeline()
