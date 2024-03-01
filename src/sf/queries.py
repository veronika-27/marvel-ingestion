create_schema = """CREATE SCHEMA IF NOT EXISTS "{sf_database}". "{sf_schema}";"""

grant_schemas = (
    """grant usage on all schemas in database "{sf_database}" to role "{sf_role}";"""
)

create_format = """create or replace file format "{sf_database}"."{sf_schema}"."FINAL_PRJ_FF" 
                        TYPE = 'CSV' SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY='"';"""

grant_ff_usage = """grant usage on file format "{sf_database}"."{sf_schema}"."FINAL_PRJ_FF" 
                          to role "{sf_role}"; """

create_storage_integration = """create storage integration IF NOT EXISTS s3_integration
                                     type = external_stage
                                     storage_provider = s3
                                     enabled = true
                                     storage_aws_role_arn = 'arn:aws:iam::{sf_iam_id}:role/{bucket_name}-SF'
                                     storage_allowed_locations = ('s3://{bucket_name}/')"""

gran_integr_usage = (
    """grant usage on integration s3_integration to role "{sf_role}"; """
)

grant_create_stage = (
    """grant create stage on schema "{sf_schema}" to role "{sf_role}"; """
)

create_stage = """CREATE OR REPLACE STAGE "{sf_database}"."{sf_schema}"."S3-STAGE"
                        URL = 's3://{bucket_name}/'
                        storage_integration = S3_INTEGRATION
                        file_format = "{sf_database}"."{sf_schema}"."FINAL_PRJ_FF" ;"""

grant_usage_stage = """grant usage on stage "{sf_database}"."{sf_schema}"."S3-STAGE" to role "{sf_role}" ;"""

grant_tables = """grant select,insert,update,delete on all tables in database "{sf_database}" to role "{sf_role}" ;"""

create_table_chars = """ CREATE TABLE IF NOT EXISTS "{sf_database}"."{sf_schema}"."{table_name}"
            (
                        id int PRIMARY KEY,
                        name varchar(1000),
                        description varchar(100000),
                        modified varchar(250),
                        modified_ts int, 
                        resourceURI varchar(1000),
                        urls varchar(1000),
                        thumbnail varchar(1000),
                        available_comics int,
                        available_stories int,
                        available_events int,
                        available_series int
            ) ; """

merge_table_chars = """MERGE INTO "{sf_database}"."{sf_schema}"."{table_name}" 
                            using "{sf_database}"."{sf_schema}"."{table_name}_INCR"
                            ON CHARACTERS.id = CHARACTERS_INCR.id 
                            AND CHARACTERS.modified_ts = CHARACTERS_INCR.modified_ts
                            WHEN NOT MATCHED THEN 
                            INSERT (id, name, description, modified, modified_ts, resourceURI, urls, thumbnail, available_comics, available_stories, available_events, available_series)
                            VALUES (CHARACTERS_INCR.id, CHARACTERS_INCR.name, CHARACTERS_INCR.description, CHARACTERS_INCR.modified, CHARACTERS_INCR.modified_ts, CHARACTERS_INCR.resourceURI, CHARACTERS_INCR.urls, CHARACTERS_INCR.thumbnail, CHARACTERS_INCR.available_comics, CHARACTERS_INCR.available_stories, CHARACTERS_INCR.available_events, CHARACTERS_INCR.available_series);
                        """

create_char_comics_rel_table = """CREATE TABLE IF NOT EXISTS "{sf_database}"."{sf_schema}"."{table_name}"
                                       (character_id int PRIMARY KEY, 
                                       comics_id int); """

merge_char_comics_rel_table = """MERGE INTO "{sf_database}"."{sf_schema}"."{table_name}" 
                                      using "{sf_database}"."{sf_schema}"."{table_name}_INCR"
                                      ON REL_CHARACTERS_COMICS.character_id = REL_CHARACTERS_COMICS_INCR.character_id
                                      AND REL_CHARACTERS_COMICS.comics_id = REL_CHARACTERS_COMICS_INCR.comics_id
                                      WHEN NOT MATCHED THEN
                                      INSERT (character_id, comics_id)
                                      VALUES (REL_CHARACTERS_COMICS_INCR.character_id, REL_CHARACTERS_COMICS_INCR.comics_id)
                                    """

create_char_events_rel_table = """CREATE TABLE IF NOT EXISTS "{sf_database}"."{sf_schema}"."{table_name}"
                                       (character_id int PRIMARY KEY, 
                                       events_id int); """

merge_char_events_rel_table = """MERGE INTO "{sf_database}"."{sf_schema}"."{table_name}" 
                                        using "{sf_database}"."{sf_schema}"."{table_name}_INCR"
                                        ON REL_CHARACTERS_EVENTS.character_id = REL_CHARACTERS_EVENTS_INCR.character_id
                                        AND REL_CHARACTERS_EVENTS.events_id = REL_CHARACTERS_EVENTS_INCR.events_id
                                        WHEN NOT MATCHED THEN
                                        INSERT (character_id, events_id)
                                        VALUES (REL_CHARACTERS_EVENTS_INCR.character_id, REL_CHARACTERS_EVENTS_INCR.events_id)
                                    """

create_table_comics = """CREATE TABLE IF NOT EXISTS "{sf_database}"."{sf_schema}"."{table_name}"
                    (
                                id int PRIMARY KEY,
                                digitalId int,
                                title varchar(1000),
                                issueNumber int,
                                variantDescription varchar(100000),
                                description char(100000),
                                modified varchar(250),
                                modified_ts int,
                                isbn varchar(2500),
                                upc varchar(2500),
                                diamondCode char(2500),
                                ean varchar(2500),
                                issn varchar(2500),
                                format char(2500),
                                pageCount int,
                                textObjects varchar(100000),
                                series varchar(10000),
                                resourceURI varchar(512),
                                urls varchar(100000),
                                variants varchar(10000),
                                collections varchar(10000),
                                collectedIssues varchar(10000),
                                dates varchar(1000),
                                prices varchar(1000),
                                thumbnail varchar(1000),
                                images varchar(100000),
                                available_creators int,
                                available_stories int,
                                available_events int,
                                available_characters int
                    ) ; """

merge_table_comics = """MERGE INTO "{sf_database}"."{sf_schema}"."{table_name}" 
                                using "{sf_database}"."{sf_schema}"."{table_name}_INCR" 
                                ON COMICS.id = COMICS.id 
                                AND COMICS.modified_ts = COMICS_INCR.modified_ts
                                WHEN NOT MATCHED THEN 
                                INSERT 
                                    (
                                        id,
                                        digitalId,
                                        title,
                                        issueNumber,
                                        variantDescription,
                                        description,
                                        modified,
                                        modified_ts,
                                        isbn,
                                        upc,
                                        diamondCode,
                                        ean,
                                        issn,
                                        format,
                                        pageCount,
                                        textObjects,
                                        series,
                                        resourceURI,
                                        urls,
                                        variants,
                                        collections,
                                        collectedIssues,
                                        dates,
                                        prices,
                                        thumbnail,
                                        images,
                                        available_creators,
                                        available_stories,
                                        available_events,
                                        available_characters
                                    ) 
                                VALUES 
                                    (
                                        COMICS_INCR.id,
                                        COMICS_INCR.digitalId,
                                        COMICS_INCR.title,
                                        COMICS_INCR.issueNumber,
                                        COMICS_INCR.variantDescription,
                                        COMICS_INCR.description,
                                        COMICS_INCR.modified,
                                        COMICS_INCR.modified_ts,
                                        COMICS_INCR.isbn,
                                        COMICS_INCR.upc,
                                        COMICS_INCR.diamondCode,
                                        COMICS_INCR.ean,
                                        COMICS_INCR.issn,
                                        COMICS_INCR.format,
                                        COMICS_INCR.pageCount,
                                        COMICS_INCR.textObjects,
                                        COMICS_INCR.series,
                                        COMICS_INCR.resourceURI,
                                        COMICS_INCR.urls,
                                        COMICS_INCR.variants,
                                        COMICS_INCR.collections,
                                        COMICS_INCR.collectedIssues,
                                        COMICS_INCR.dates,
                                        COMICS_INCR.prices,
                                        COMICS_INCR.thumbnail,
                                        COMICS_INCR.images,
                                        COMICS_INCR.available_creators,
                                        COMICS_INCR.available_stories,
                                        COMICS_INCR.available_events,
                                        COMICS_INCR.available_characters
                                    );"""

create_table_creators = """CREATE TABLE IF NOT EXISTS "{sf_database}"."{sf_schema}"."{table_name}"
                                (
                                    id int PRIMARY KEY,
                                    firstName varchar(1000),
                                    middleName varchar(1000),
                                    lastName varchar(1000),
                                    suffix varchar(2500),
                                    fullName varchar(10000),
                                    modified varchar(250),
                                    modified_ts int, 
                                    resourceURI varchar(2500),
                                    urls varchar(10000),
                                    thumbnail varchar(1000),
                                    available_comics int,
                                    available_stories int,
                                    available_events int,
                                    available_series int
                                ) ; """

merge_table_creators = """MERGE INTO "{sf_database}"."{sf_schema}"."{table_name}"
                                using "{sf_database}"."{sf_schema}"."{table_name}_INCR" 
                                ON CREATORS.id = CREATORS_INCR.id 
                                AND CREATORS.modified_ts = CREATORS_INCR.modified_ts
                                WHEN NOT MATCHED THEN 
                                    INSERT 
                                    (
                                        id,
                                        firstName,
                                        middleName,
                                        lastName,
                                        suffix,
                                        fullName,
                                        modified,
                                        modified_ts, 
                                        resourceURI,
                                        urls,
                                        thumbnail,
                                        available_comics,
                                        available_stories,
                                        available_events,
                                        available_series
                                    ) 
                                    VALUES 
                                    (
                                        CREATORS_INCR.id,
                                        CREATORS_INCR.firstName,
                                        CREATORS_INCR.middleName,
                                        CREATORS_INCR.lastName,
                                        CREATORS_INCR.suffix,
                                        CREATORS_INCR.fullName,
                                        CREATORS_INCR.modified,
                                        CREATORS_INCR.modified_ts, 
                                        CREATORS_INCR.resourceURI,
                                        CREATORS_INCR.urls,
                                        CREATORS_INCR.thumbnail,
                                        CREATORS_INCR.available_comics,
                                        CREATORS_INCR.available_stories,
                                        CREATORS_INCR.available_events,
                                        CREATORS_INCR.available_series
                                    ); """

create_creators_comics_rel_table = """CREATE TABLE IF NOT EXISTS "{sf_database}"."{sf_schema}"."{table_name}"
                                            (creators_id int PRIMARY KEY, 
                                            comics_id int); """

merge_creators_comics_rel_table = """MERGE INTO "{sf_database}"."{sf_schema}"."{table_name}"
                                            using "{sf_database}"."{sf_schema}"."{table_name}_INCR"
                                            ON REL_CREATORS_COMICS.creators_id = REL_CREATORS_COMICS_INCR.creators_id
                                            AND REL_CREATORS_COMICS.comics_id = REL_CREATORS_COMICS_INCR.comics_id
                                            WHEN NOT MATCHED THEN
                                            INSERT (creators_id, comics_id)
                                            VALUES (REL_CREATORS_COMICS_INCR.creators_id, REL_CREATORS_COMICS_INCR.comics_id)
                                        """

create_table_events = """CREATE TABLE IF NOT EXISTS "{sf_database}"."{sf_schema}"."{table_name}"
                              ( 
                                id int PRIMARY KEY,
                                title varchar(2000),
                                description varchar(10000),
                                resourceURI varchar(2500),
                                urls varchar(10000),
                                modified varchar(250),
                                modified_ts int,
                                "start" varchar(250),
                                "end" varchar(250),
                                thumbnail varchar(1000),
                                available_comics int,
                                available_stories int,
                                available_series int,
                                available_characters int,
                                available_creators int, 
                                next varchar(2500),
                                previous varchar(2500)
                                ) ; """

merge_table_events = """MERGE INTO "{sf_database}"."{sf_schema}"."{table_name}"
                            using "{sf_database}"."{sf_schema}"."{table_name}_INCR" 
                            ON EVENTS.id = EVENTS_INCR.id 
                            AND EVENTS.modified_ts = EVENTS_INCR.modified_ts
                            WHEN NOT MATCHED THEN 
                                INSERT 
                                (
                                    id,
                                    title,
                                    description,
                                    resourceURI,
                                    urls,
                                    modified,
                                    modified_ts,
                                    "start",
                                    "end",
                                    thumbnail,
                                    available_comics,
                                    available_stories,
                                    available_series,
                                    available_characters,
                                    available_creators, 
                                    next,
                                    previous
                                ) 
                                VALUES 
                                (
                                    EVENTS_INCR.id,
                                    EVENTS_INCR.title,
                                    EVENTS_INCR.description,
                                    EVENTS_INCR.resourceURI,
                                    EVENTS_INCR.urls,
                                    EVENTS_INCR.modified,
                                    EVENTS_INCR.modified_ts,
                                    EVENTS_INCR."start",
                                    EVENTS_INCR."end",
                                    EVENTS_INCR.thumbnail,
                                    EVENTS_INCR.available_comics,
                                    EVENTS_INCR.available_stories,
                                    EVENTS_INCR.available_series,
                                    EVENTS_INCR.available_characters,
                                    EVENTS_INCR.available_creators, 
                                    EVENTS_INCR.next,
                                    EVENTS_INCR.previous
                                ); """

create_table_series = """ CREATE TABLE IF NOT EXISTS "{sf_database}"."{sf_schema}"."{table_name}"
                                (
                                    id int PRIMARY KEY,
                                    title varchar(10000),
                                    description varchar(50000),
                                    resourceURI varchar(25000),
                                    urls varchar(2500),
                                    startYear varchar(250),
                                    endYear varchar(250),
                                    rating varchar(2500),
                                    modified varchar(250),
                                    modified_ts int, 
                                    thumbnail varchar(1000),
                                    available_comics int,
                                    available_stories int,
                                    available_events int,
                                    available_characters int,
                                    available_creators int, 
                                    next varchar(2500),
                                    previous varchar(2500)
                                ) ; """

merge_table_series = """MERGE INTO "{sf_database}"."{sf_schema}"."{table_name}" 
                                using "{sf_database}"."{sf_schema}"."{table_name}_INCR" 
                                ON SERIES.id = SERIES_INCR.id 
                                AND SERIES.modified_ts = SERIES_INCR.modified_ts
                                WHEN NOT MATCHED THEN 
                                    INSERT 
                                    (
                                        id,
                                        title,
                                        description,
                                        resourceURI,
                                        urls,
                                        startYear,
                                        endYear,
                                        rating,
                                        modified,
                                        modified_ts, 
                                        thumbnail,
                                        available_comics,
                                        available_stories,
                                        available_events,
                                        available_characters,
                                        available_creators, 
                                        next,
                                        previous
                                    ) 
                                    VALUES 
                                    (
                                        SERIES_INCR.id,
                                        SERIES_INCR.title,
                                        SERIES_INCR.description,
                                        SERIES_INCR.resourceURI,
                                        SERIES_INCR.urls,
                                        SERIES_INCR.startYear,
                                        SERIES_INCR.endYear,
                                        SERIES_INCR.rating,
                                        SERIES_INCR.modified,
                                        SERIES_INCR.modified_ts, 
                                        SERIES_INCR.thumbnail,
                                        SERIES_INCR.available_comics,
                                        SERIES_INCR.available_stories,
                                        SERIES_INCR.available_events,
                                        SERIES_INCR.available_characters,
                                        SERIES_INCR.available_creators, 
                                        SERIES_INCR.next,
                                        SERIES_INCR.previous
                                    ); """

create_table_stories = """CREATE TABLE IF NOT EXISTS "{sf_database}"."{sf_schema}"."{table_name}"
                               (
                                    id int PRIMARY KEY,
                                    title varchar(1000),
                                    description varchar(100000),
                                    resourceURI varchar(2500),
                                    type char(250),
                                    modified varchar(250),
                                    modified_ts int,
                                    thumbnail varchar(1000),
                                    available_comics int,
                                    available_series int,
                                    available_events int,
                                    available_characters int,
                                    available_creators int, 
                                    originalIssue varchar(1000)
                               ); """

merge_table_stories = """MERGE INTO "{sf_database}"."{sf_schema}"."{table_name}" 
                                using "{sf_database}"."{sf_schema}"."{table_name}_INCR" 
                                ON STORIES.id = STORIES_INCR.id 
                                AND STORIES.modified_ts = STORIES_INCR.modified_ts
                                WHEN NOT MATCHED THEN 
                                    INSERT 
                                    (
                                        id,
                                        title,
                                        description,
                                        resourceURI,
                                        type,
                                        modified,
                                        modified_ts,
                                        thumbnail,
                                        available_comics,
                                        available_series,
                                        available_events,
                                        available_characters,
                                        available_creators, 
                                        originalIssue
                                    ) 
                                    VALUES 
                                    (
                                        STORIES_INCR.id,
                                        STORIES_INCR.title,
                                        STORIES_INCR.description,
                                        STORIES_INCR.resourceURI,
                                        STORIES_INCR.type,
                                        STORIES_INCR.modified,
                                        STORIES_INCR.modified_ts,
                                        STORIES_INCR.thumbnail,
                                        STORIES_INCR.available_comics,
                                        STORIES_INCR.available_series,
                                        STORIES_INCR.available_events,
                                        STORIES_INCR.available_characters,
                                        STORIES_INCR.available_creators, 
                                        STORIES_INCR.originalIssue
                                    ); """

copy_data_into_sf = """COPY INTO "{sf_database}"."{sf_schema}"."{table_name}"
from @"{sf_database}"."{sf_schema}"."S3-STAGE"/ingest_data/{csv_name}.csv SIZE_LIMIT = 490000000;"""

sf_truncate = """TRUNCATE "{sf_database}"."{sf_schema}"."{table_name}";"""
