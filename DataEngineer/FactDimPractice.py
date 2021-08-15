import psycopg2

try:
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=first_db password=Mrbhturner95!"
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

try:
    cur.execute("DROP table fact_table")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table items_purchased")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table store")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table customer")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)

try:
    cur.execute(
        "create table if not exists fact_table (customer_id int, store_id int, spent real)"
    )
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

# Insert into all tables
try:
    cur.execute(
        "insert into fact_table \
        values (%s, %s, %s)",
        (1, 1, 20.50),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)
try:
    cur.execute(
        "insert into fact_table \
    values (%s, %s, %s)",
        (2, 1, 35.21),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "create table items_purchased (customer_id int, item_id int, item_name text)"
    )
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute(
        "insert into items_purchased \
        values (%s, %s, %s)",
        (1, 1, "Rubber Soul"),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "insert into items_purchased \
        values (%s, %s, %s)",
        (2, 3, "Let it Be"),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("create table store (store_id int, state text)")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("insert into store values (%s, %s)", (1, "CA"))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)
try:
    cur.execute("insert into store values (%s, %s)", (2, "WA"))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("create table customer (customer_id int, name text, rewards text)")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("insert into customer values (%s, %s, %s)", (1, "Amanda", "Y"))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("insert into customer values (%s, %s, %s)", (2, "Toby", "N"))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)
