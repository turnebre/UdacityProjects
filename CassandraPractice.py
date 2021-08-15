import cassandra

from cassandra.cluster import Cluster

try:
    cluster = Cluster()  # If you have a locally installed Apache Cassandra instance
    session = cluster.connect()
except Exception as e:
    print(e)

## TO-DO: Create the keyspace
try:
    session.execute(
        """
    CREATE KEYSPACE IF NOT EXISTS cass 
    WITH REPLICATION = 
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
    )

except Exception as e:
    print(e)

    ## To-Do: Add in the keyspace you created
try:
    session.set_keyspace("cass")
except Exception as e:
    print(e)

try:
    session.execute("drop table songs")
except Exception as e:
    print(e)

## TO-DO: Complete the query below
query = "CREATE TABLE IF NOT EXISTS songs "
query = (
    query
    + "(year int, song_title text, artist_name text, album_name text, single boolean, PRIMARY KEY (year, artist_name))"
)
try:
    session.execute(query)
except Exception as e:
    print(e)

## Add in query and then run the insert statement
query = "insert into songs (year, song_title, artist_name, album_name, single)"
query = query + " VALUES (%s, %s, %s, %s, %s)"

try:

    session.execute(
        query,
        (1970, "Across The Universe", "The Beatles", "Let It Be", False),
    )
except Exception as e:
    print(e)

try:
    session.execute(
        query, (1965, "Think For Yourself", "The Beatles", "Rubber Soul", False)
    )
except Exception as e:
    print(e)
