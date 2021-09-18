# Cloud Datawarehouse Project

This project looks at Sparkify's data collection of song's and listening activity.  The goal is to move their data, which resides in S3 in a directory of JSON logs, to a cloud database (redshift).

The `"dwh.cfg"` file contains all the AWS credentials needed to connect to our database, such as the hist, S3 path, and cluster configuration

## Database Schema Design

The database schema is broken down into fact and dimension tables.  Most of the columns have non null constraints, but a few didnt have much information so were left without a non null constraint.  The schema goes as follows:

#### songplays

  - This is the fact table for this schema.  it contains the primary keys for all the dimensional tables along with the start_time for each listening session.

#### users

  -  Contains user information, such as first & last name, gender, and level.
 
  
#### songs

  - Contains information on each song, such as title, artist_id, year and duration.
  
#### artists 

  - Contains  information relating to song artists, such as their name and location.
  
#### time

  - Contains information based on the time of each songplay.  It breaks down the hour, day, week , month, weekday etc.  


## ETL Pipeline

The `"create_tables.py"` script contains all the queries to create the tables needed for the schema.  The ETL pipeline (`"etl.py"`) will automate through the S3 directory and i tnsert the parsed JSON files into a staged tables.  Each script has its own purpose throughtout the etl pipeline.  Lastly, the `"dwh.cfg"` file contains all the information relating to the Redshift Warehouse, such as the Cluster, Credentials, and S3 location.  