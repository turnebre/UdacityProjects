import psycopg2

try:
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=studentdb user=student password=student"
    )
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)
