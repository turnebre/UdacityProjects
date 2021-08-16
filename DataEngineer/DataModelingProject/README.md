# Relational Data Modeling Project

This project looks at Sparkify's data collection of song's and user activity for their new streaming app.  The goal is to allow the analytics teams to analyze this data to understand what users are listening to They decided they want a Postgres database from the json logs theyhave on song and user data.  To do this, we'll create an ETL pipeline in python and PostgresSQL to parse the json files and create an inuitive database for ther analytics teams to utilize.

### Database Schema Design

For starters, we'll define the database schema using a star schema.  A star schema has fact and dimension tables with the fact data for Sparkify being the songplays table, and the dimension tables will be songs, artists, users, and time.  The songplays table will be records in log data associated with song plays, such as starttime, user id, artist id, etc.  The dimension tables will have further information on users, artist, songs, and time such as user name and gender, artist name and location, etc.

### ETL Pipeline

The ETL pipeline will be automated to loop through the dataset files and create the database, tables, and data. Each script has its own purpose throughtout the etl pipeline. 

- `"sql_queries.py"`

  - This script contains all the queries used to create the database, tables, and table insertions.  Its imported as a module in the etl pipeline and called at its respective step.

- `"create_tables.py"`

  - This is used recreate the database prior to each run to ensure all data is entered correctly.
 
  
- `"etl.ipynb"` 

  - Used to create the etl process for each table.  This is a python notebook that was used to create test the etl process and parse the data.
  
- `"etl.py"` 

  - This is the final script run to create the entire database.  This is only run once the notebook version validates the code is correct with no errors or discrepencies.  
  
- `"test.ipynb"` 

  - This used a sql extension to pull data from each table and usnure that they were correctly made.  Allows us to run any sql query we could run in postgres.
