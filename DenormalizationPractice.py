import psycopg2

try:
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=first_db user=postgres password=Mrbhturner95!"
    )
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)
try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get cursor to the Database")
    print(e)
conn.set_session(autocommit=True)

# TO-DO: Create all tables
try:
    cur.execute(
        "create table if not exists transactions3 (transaction_id int, customer_name text, cashier_id int, year int, amount_spent int)"
    )
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

# Insert data into all tables

try:
    cur.execute(
        "INSERT INTO transactions3 (transaction_id, customer_name, cashier_id, year, amount_spent) \
                 VALUES (%s, %s, %s, %s, %s)",
        (1, "Amanda", 1, 2000, 40),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO transactions3 (transaction_id, customer_name, cashier_id, year, amount_spent) \
                 VALUES (%s, %s, %s, %s, %s)",
        (2, "Toby", 1, 2000, 19),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO transactions3 (transaction_id, customer_name, cashier_id, year, amount_spent) \
                 VALUES (%s, %s, %s, %s, %s)",
        (3, "Max", 2, 2018, 45),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)
