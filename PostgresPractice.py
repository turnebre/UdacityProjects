import psycopg2

try:
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=Mrbhturner95!"
    )
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get curser to the Database")
    print(e)

# TO-DO: set automatic commit to be true
conn.set_session(autocommit=True)

## TO-DO: Add the database name within the CREATE DATABASE statement. You can choose your own db name.
try:
    cur.execute("create database first_db")
except psycopg2.Error as e:
    print(e)
