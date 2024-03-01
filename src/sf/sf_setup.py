import snowflake.connector
from sf.queries import *


class ConnectionToSFError(RuntimeError):
    pass


class SqlExecution:
    """
    Class to represent SqlExecution object
    ....

    Methods:
    -----
    create_schema: creates the schema needed and handles the permission related to its usage
    create_file_format: creates the file format needed and respective permissions
    create_storage_integration: creates storage integration named s3_integration and respective permissions
    create_s3_stage: creates the s3 external stage named "S3-STAGE" and respective permissions to be used
    sf_tables_creation: creates all the tables needed to load the data from the API into SF and privileges needed
    copy_data_into_sf: applies "copy into" concrete SF table from the external stage - S3 bucket
    """

    def __init__(
        self,
        sf_account,
        sf_username,
        sf_role,
        sf_password,
        sf_warehouse,
        sf_database,
        sf_schema,
        sf_iam_id,
        bucket_name,
    ):
        try:
            self.ctx = snowflake.connector.connect(
                user=sf_username,
                password=sf_password,
                account=sf_account,
                warehouse=sf_warehouse,
                database=sf_database,
                role=sf_role,
            )
            self.role = sf_role
            self.warehouse = sf_warehouse
            self.database = sf_database
            self.account = sf_account
            self.username = sf_username
            self.password = sf_password
            self.schema = sf_schema
            self.sf_iam_id = sf_iam_id
            self.bucket_name = bucket_name

        except:
            raise ConnectionToSFError()

    def create_schema(self):
        """
        Method that creates specific schema and grants usage of schemas to specific role
        """
        con = self.ctx.cursor()
        try:

            con.execute(
                create_schema.format(
                    sf_database=self.database, sf_schema=self.schema
                )
            )
            con.execute(
                grant_schemas.format(sf_database=self.database, sf_role=self.role)
            )
        except Exception as e:
            print("Problem when creating the schema! Error : " + str(e))
            raise e

        con.close()

    def create_file_format(self):
        """
        Method that creates needed csv file format and grants usage of it to specific SF_role
        """
        con = self.ctx.cursor()

        try:
            con.execute(
                create_format.format(
                    sf_database=self.database, sf_schema=self.schema
                )
            )
            con.execute(
                grant_ff_usage.format(
                    sf_database=self.database, sf_schema=self.schema, sf_role=self.role
                )
            )
        except Exception as e:
            print("Problem when creating the file format! Error : " + str(e))
            raise e

        con.close()

    def create_storage_integration(self):
        """
        Creates specific storage integration named: s3_integration with previously created aws role:
        il-tapde-final-exercise-veronika-SF and s3 bucket: il-tapde-final-exercise-veronika and grants usage of it
        to specific SF_role
        """
        con = self.ctx.cursor()
        try:
            con.execute(
                create_storage_integration.format(
                    bucket_name=self.bucket_name, sf_iam_id=self.sf_iam_id
                )
            )
            con.execute(gran_integr_usage.format(sf_role=self.role))
        except Exception as e:
            print("Problem when creating storage integration! Error : " + str(e))
            raise e

        con.close()

    def create_s3_stage(self):
        """
        Creates stage in SF named: S3-STAGE based on s3 bucket and previously created storage integration: S3_INTEGRATION
        """
        con = self.ctx.cursor()
        try:
            con.execute(
                grant_create_stage.format(sf_schema=self.schema, sf_role=self.role)
            )
            con.execute(
                create_stage.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    bucket_name=self.bucket_name,
                )
            )
            con.execute(
                grant_usage_stage.format(
                    sf_database=self.database, sf_schema=self.schema, sf_role=self.role
                )
            )
        except Exception as e:
            print("Problem when creating stage! Error : " + str(e))
            raise e

        con.close()

    def sf_tables_creation(self):
        """
        Creates all the tables in SF that will be used to ingest the data and the relations from the API
        and grants select,insert,update,delete on all tables in selected database to selected role
        """
        con = self.ctx.cursor()
        con.execute(
            grant_tables.format(sf_database=self.database, sf_role=self.role)
        )
        try:
            con.execute(
                create_table_chars.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="CHARACTERS",
                )
            )
            con.execute(
                create_table_chars.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="CHARACTERS_INCR",
                )
            )
            con.execute(
                create_char_comics_rel_table.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="REL_CHARACTERS_COMICS",
                )
            )
            con.execute(
                create_char_comics_rel_table.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="REL_CHARACTERS_COMICS_INCR",
                )
            )
            con.execute(
                create_char_events_rel_table.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="REL_CHARACTERS_EVENTS",
                )
            )
            con.execute(
                create_char_events_rel_table.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="REL_CHARACTERS_EVENTS_INCR",
                )
            )

            con.execute(
                create_table_comics.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="COMICS",
                )
            )

            con.execute(
                create_table_comics.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="COMICS_INCR",
                )
            )
            con.execute(
                create_table_creators.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="CREATORS",
                )
            )
            con.execute(
                create_table_creators.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="CREATORS_INCR",
                )
            )
            con.execute(
                create_creators_comics_rel_table.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="REL_CREATORS_COMICS",
                )
            )
            con.execute(
                create_creators_comics_rel_table.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="REL_CREATORS_COMICS_INCR",
                )
            )

            con.execute(
                create_table_events.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="EVENTS",
                )
            )
            con.execute(
                create_table_events.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="EVENTS_INCR",
                )
            )
            con.execute(
                create_table_series.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="SERIES",
                )
            )
            con.execute(
                create_table_series.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="SERIES_INCR",
                )
            )
            con.execute(
                create_table_stories.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="STORIES",
                )
            )
            con.execute(
                create_table_stories.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="STORIES_INCR",
                )
            )
        except Exception as e:
            print("Problem when creating needed tables in SF! Error : " + str(e))
            raise e

        con.close()

    def sf_tables_merge(self):
        """
        Merges all the incremental data from _INCR to the full data tables
        """
        con = self.ctx.cursor()
        try:
            con.execute(
                merge_table_chars.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="CHARACTERS",
                )
            )
            con.execute(
                merge_char_comics_rel_table.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="REL_CHARACTERS_COMICS",
                )
            )
            con.execute(
                merge_char_events_rel_table.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="REL_CHARACTERS_EVENTS",
                )
            )

            con.execute(
                merge_table_comics.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="COMICS",
                )
            )
            con.execute(
                merge_table_creators.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="CREATORS",
                )
            )
            con.execute(
                merge_creators_comics_rel_table.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="REL_CREATORS_COMICS",
                )
            )

            con.execute(
                merge_table_events.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="EVENTS",
                )
            )
            con.execute(
                merge_table_series.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="SERIES",
                )
            )
            con.execute(
                merge_table_stories.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name="STORIES",
                )
            )
        except Exception as e:
            print("Problem to merge tables with incremental data! Error : " + str(e))
            raise e

        con.close()

    def truncate_sf_table(self, table_name):
        """
        Truncates the data from SF table
        """
        con = self.ctx.cursor()
        try:
            con.execute(
                sf_truncate.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name=table_name.upper(),
                )
            )
        except Exception as e:
            print("Problem to truncate table! Error : " + str(e))
            raise e

        con.close()

    def copy_data_into_sf(self, table_name, csv_name=""):
        """
        Copies/Inserts the data from S3 bucket to specific SF table
        """
        if csv_name == "":
            csv_name = table_name

        con = self.ctx.cursor()
        try:
            con.execute(
                copy_data_into_sf.format(
                    sf_database=self.database,
                    sf_schema=self.schema,
                    table_name=table_name.upper(),
                    csv_name=csv_name,
                )
            )
        except Exception as e:
            print("Problem to insert the data! Error : " + str(e))
            raise e

        con.close()

    def sf_s3_initial_setup(self):
        """
        Function that combines all the steps needed to successfully create the tables  needed for data ingestion
         form S3 bucket to SF
        """

        self.create_schema()
        self.create_file_format()
        self.create_storage_integration()
        self.create_s3_stage()
        self.sf_tables_creation()
        print("Tables created successfully")
