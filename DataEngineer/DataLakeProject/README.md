# Data Lakes with Spark Project

### Discuss the purpose of this database in context of the startup, Sparkify, and their analytical goals.

This database is designed to allow Sparkify to analyze their data via dimensional tables.  The data resides in s3 as json logs, and is modeled into 5 fact and dimensional tables.  It'll empower the analytics team to continue their analysis on Sparkifys data.  

### State and justify your database schema design and ETL pipeline.

Fact and dimensional tables allow for quick and efficient querying this database.  It allows the analytics team to analyze events and add the appropriate dimensions with just one or more joins.  

Spark is a powerful data processing framework run accross a given cluster.  In this case, we created the cluster using an AWS EMR instance of 3 nodes.  This allows for faster processing of big data through parallel processing, especially when dealing with the song, log, and time tables.

## Database Schema Design

The database schema is broken down into fact and dimension tables, the schema goes as follows:

#### songplays

  - This is the fact table for this schema.  it contains the primary keys for all the dimensional tables along with the start_time for each listening session.

#### users

  -  Contains user information, such as first & last name, gender, and level.
  
#### songs

  - Contains information on each song, such as title, artist_id, year and duration.
  
#### artists 

  - Contains  information relating to song artists, such as their name and location.

## Script Instructions

In order to run above script, a number of items need to be completed. First, and EMR cluster configured to run Spark needs to be created in AWS.  Second, A S3 bucket needs to be made where the modeled data will be stored.  Third, an IAM role needs to be made with AWS access and secret keys in order to connect, read, and write to the cluster/ S3 bucket which'll be stored in the '"dl.cfg"' file.  Once this is all complete, you'll need to get the end point for the S3 bucket, store it as a variable in the script, and run the '"etl.py"' file.