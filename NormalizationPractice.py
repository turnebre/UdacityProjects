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

try:
    cur.execute("DROP table music_store")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table music_store2")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table albums_sold")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table employees")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table transactions")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table transactions2")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)
try:
    cur.execute("DROP table sales")
except psycopg2.Error as e:
    print("Error: Dropping table")
    print(e)

# We Create Table Statement and insert the data in the table
try:
    cur.execute(
        "CREATE TABLE IF NOT EXISTS music_store (transaction_id int, \
                                                         customer_name varchar, cashier_name varchar, \
                                                         year int, albums_purchased text[]);"
    )
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute(
        "INSERT INTO music_store (transaction_id, customer_name, cashier_name, year, albums_purchased) \
                 VALUES (%s, %s, %s, %s, %s)",
        (1, "Amanda", "Sam", 2000, ["Rubber Soul", "Let it Be"]),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO music_store (transaction_id, customer_name, cashier_name, year, albums_purchased) \
                 VALUES (%s, %s, %s, %s, %s)",
        (2, "Toby", "Sam", 2000, ["My Generation"]),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO music_store (transaction_id, customer_name, cashier_name, year, albums_purchased) \
                 VALUES (%s, %s, %s, %s, %s)",
        (3, "Max", "Bob", 2018, ["Meet the Beatles", "Help!"]),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)


try:
    cur.execute("SELECT * FROM music_store;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

try:
    cur.execute(
        "CREATE TABLE IF NOT EXISTS music_store2 (transaction_id int, \
                                                         customer_name varchar, cashier_name varchar, \
                                                         year int, albums_purchased text);"
    )
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute(
        "INSERT INTO music_store2 (transaction_id, customer_name, cashier_name, year, albums_purchased) \
                 VALUES (%s, %s, %s, %s, %s)",
        (1, "Amanda", "Sam", 2000, "Rubber Soul"),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO music_store2 (transaction_id, customer_name, cashier_name, year, albums_purchased) \
                 VALUES (%s, %s, %s, %s, %s)",
        (1, "Amanda", "Sam", 2000, "Let it Be"),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO music_store2 (transaction_id, customer_name, cashier_name, year, albums_purchased) \
                 VALUES (%s, %s, %s, %s, %s)",
        (2, "Toby", "Sam", 2000, "My Generation"),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO music_store2 (transaction_id, customer_name, cashier_name, year, albums_purchased) \
                 VALUES (%s, %s, %s, %s, %s)",
        (3, "Max", "Bob", 2018, "Help!"),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO music_store2 (transaction_id, customer_name, cashier_name, year, albums_purchased) \
                 VALUES (%s, %s, %s, %s, %s)",
        (3, "Max", "Bob", 2018, "Meet the Beatles"),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute("SELECT * FROM music_store2;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

    # We create two new tables transactions and albums sold and insert data into these tables

try:
    cur.execute(
        "CREATE TABLE IF NOT EXISTS transactions (transaction_id int, \
                                                           customer_name varchar, cashier_name varchar, \
                                                           year int);"
    )
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute(
        "CREATE TABLE IF NOT EXISTS albums_sold (album_id int, transaction_id int, \
                                                          album_name varchar);"
    )
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute(
        "INSERT INTO transactions (transaction_id, customer_name, cashier_name, year) \
                 VALUES (%s, %s, %s, %s)",
        (1, "Amanda", "Sam", 2000),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO transactions (transaction_id, customer_name, cashier_name, year) \
                 VALUES (%s, %s, %s, %s)",
        (2, "Toby", "Sam", 2000),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO transactions (transaction_id, customer_name, cashier_name, year) \
                 VALUES (%s, %s, %s, %s)",
        (3, "Max", "Bob", 2018),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)",
        (1, 1, "Rubber Soul"),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)",
        (2, 1, "Let it Be"),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)",
        (3, 2, "My Generation"),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)",
        (4, 3, "Meet the Beatles"),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)",
        (5, 3, "Help!"),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

# We complete the join on the transactions and album_sold tables

try:
    cur.execute(
        "CREATE TABLE IF NOT EXISTS transactions2 (transaction_id int, \
                                                           customer_name varchar, cashier_id int, \
                                                           year int);"
    )
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute(
        "CREATE TABLE IF NOT EXISTS employees (employee_id int, \
                                                       employee_name varchar);"
    )
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute(
        "INSERT INTO transactions2 (transaction_id, customer_name, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)",
        (1, "Amanda", 1, 2000),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO transactions2 (transaction_id, customer_name, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)",
        (2, "Toby", 1, 2000),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO transactions2 (transaction_id, customer_name, cashier_id, year) \
                 VALUES (%s, %s, %s, %s)",
        (3, "Max", 2, 2018),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO employees (employee_id, employee_name) \
                 VALUES (%s, %s)",
        (1, "Sam"),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "INSERT INTO employees (employee_id, employee_name) \
                 VALUES (%s, %s)",
        (2, "Bob"),
    )
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)

try:
    cur.execute(
        "create table if not exists sales (transaction_id int, amount_spent int)"
    )
except psycopg2.Error as e:
    print("Error: Could not create table")
    print(e)

try:
    cur.execute(
        "insert into sales (transaction_id, amount_spent) \
        values (%s, %s)",
        (1, 40),
    )
except psycopg2.Error as e:
    print("Error: Could not insert")
    print(e)

try:
    cur.execute(
        "insert into sales (transaction_id, amount_spent) \
        values (%s, %s)",
        (2, 19),
    )
except psycopg2.Error as e:
    print("Error: Could not insert")
    print(e)

try:
    cur.execute(
        "insert into sales (transaction_id, amount_spent) \
        values (%s, %s)",
        (3, 45),
    )
except psycopg2.Error as e:
    print("Error: Could not insert")
    print(e)

try:
    cur.execute(
        "select a.transaction_id, a.customer_name, d.employee_id, a.year, b.album_id, c.amount_spent \
        from transactions2 a \
        left join albums_sold b \
        on a.transaction_id = b.transaction_id \
        left join sales c \
        on a.transaction_id = c.transaction_id \
        left join employees d \
        on a.cashier_id = d.employee_id"
    )
except psycopg2.Error as e:
    print("Error: Could group")
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()
