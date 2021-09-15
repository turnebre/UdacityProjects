import configparser


# CONFIG
config = configparser.ConfigParser()
config.read("dwh.cfg")

# DROP TABLES

staging_events_table_drop = "drop table if exists staging_events"
staging_songs_table_drop = "drop table if exists staging_songs"
songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists sings"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES


staging_events_table_create = """
CREATE TABLE IF NOT EXISTS staging_events (
    artist text,
    auth text,
    firstName text,
    gender text,
    itemInSession int,
    length decimal,
    level text,
    location text,
    method text,
    page text,
    registration text,
    sessionId int,
    song text,
    status int,
    userAgent text,
    userId int
)
"""

staging_songs_table_create = """
CREATE TABLE if not exists staging_events (
    num_songs int, 
    artist_id text,
    artist_latitude decimal,
    artist_location text,
    artist_name text,
    song_id text,
    title text,
    duration decimal,
    year int)
"""

songplay_table_create = """
"""

user_table_create = """
"""

song_table_create = """
"""

artist_table_create = """
"""

time_table_create = """
"""

# STAGING TABLES

staging_events_copy = (
    """
"""
).format()

staging_songs_copy = (
    """
"""
).format()

# FINAL TABLES

songplay_table_insert = """
"""

user_table_insert = """
"""

song_table_insert = """
"""

artist_table_insert = """
"""

time_table_insert = """
"""

# QUERY LISTS

create_table_queries = [
    staging_events_table_create,
    staging_songs_table_create,
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
]
drop_table_queries = [
    staging_events_table_drop,
    staging_songs_table_drop,
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [
    songplay_table_insert,
    user_table_insert,
    song_table_insert,
    artist_table_insert,
    time_table_insert,
]
