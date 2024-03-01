# Marvel API ingestion pipeline

In this repo you can find the code for the ingestion of all Marvel entities, as well as, 
python code dedicated to the initial Snowflake setup needed for the ingestion (very simple IaC).

The pipeline flow:

  ![Ingestion FLow](https://github.com/veronika-27/marvel-ingestion/assets/64424805/5fd6b512-d2fe-4463-a8dd-228570016946)

The data from the API is ingested into the Snowflake using an S3 bucket (as external stage).
                                                                                                 
The main aims: 
                  
- all the data for all the entities(Characters, Comics, Creators, Events, Series and Stories) is ingested into dedicated table
- the pipeline is idempotent and handles failures gracefully
- some unit tests are inplace in order to achieve certain code coverage
- there is certain flexibility (deployment into multiple environments is ensured)

Within the src folder can be found: 
- the files, named after each Marvel entity; 
- metadata.py - Metadata class that helps us keep track of the current ingestion (in order to ensure the idempotency)
- sf: code base for the initial Snowflake setup (simple IaC via python)
- aws: python code for AWS setup (IAM roles and permissions, and some python methods to interact with the S3 bucket (based on boto3)

The unit tests can be found in the folder of the same name. 

The ingestion pipeline is packaged into docker image (based on the existing Dockerfile) and there is a gitlab-ci.yml 

for the CI pipeline with all the steps to test and build the data ingestion pipeline (as gitlab repo was used initially)
