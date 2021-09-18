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
    lastName text,
    length decimal,
    level text,
    location text,
    method text,
    page text,
    registration text,
    sessionId int,
    song text,
    status int,
    ts bigint,
    userAgent text,
    userId int
)
"""

staging_songs_table_create = """
CREATE TABLE if not exists staging_songs (
    num_songs int, 
    artist_id text,
    artist_latitude decimal,
    artist_longitude decimal,
    artist_location text,
    artist_name text,
    song_id text,
    title text,
    duration decimal,
    year int)
"""

songplay_table_create = """
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id int IDENTITY (0,1),
    start_time timestamp not null,
    user_id int,
    level text not null,
    song_id text not null,
    artist_id text not null,
    session_id int,
    location text not null,
    user_agent text,
    primary key(songplay_id)
)
"""

user_table_create = """
CREATE TABLE IF NOT EXISTS users (
    user_id int IDENTITY(0,1),
    first_name text not null,
    last_name text not null,
    gender text not null,
    level text not null,
    primary key(user_id)
)
"""

song_table_create = """
CREATE TABLE IF NOT EXISTS songs (
    song_id text,
    title text not null,
    artist_id text not null,
    year int not null,
    duration decimal not null,
    primary key(song_id)
)
"""

artist_table_create = """
CREATE TABLE IF NOT EXISTS artists (
    artist_id text,
    name text not null,
    location text,
    latitude decimal,
    longitude decimal,
    primary key(artist_id)
)
"""

time_table_create = """
CREATE TABLE IF NOT EXISTS time (
    start_time timestamp not null,
    hour int not null,
    day int not null,
    week int not null,
    month int not null,
    year int not null,
    weekday int not null
)
"""

# STAGING TABLES

staging_events_copy = (
    """
COPY staging_events
FROM 's3://udacity-dend/log_data'
credentials 'aws_iam_role={}'
format as json 'auto'
"""
).format("arn:aws:iam::071889381944:role/myRedshiftRole")

staging_songs_copy = (
    """
COPY staging_songs
FROM 's3://udacity-dend/song_data'
credentials 'aws_iam_role={}'
format as json 'auto'
"""
).format("arn:aws:iam::071889381944:role/myRedshiftRole")

# FINAL TABLES

songplay_table_insert = """
INSERT INTO songplays (
    start_time,
    user_id,
    level,
    song_id,
    artist_id,
    session_id,
    location,
    user_agent
) ( 
    SELECT 
        (timestamp 'epoch' + a.ts::numeric / 1000 * interval '1 second'),
        a.userid,
        a.level,
        b.song_id,
        b.artist_id,
        a.sessionid,
        a.location,
        a.useragent
    FROM staging_events a
    LEFT JOIN staging_songs b
    ON a.artist = b.artist_name
    and a.song = b.title
    where b.song_id is not null
)
"""

user_table_insert = """
INSERT INTO users (
    first_name,
    last_name,
    gender,
    level 
) (
    SELECT 
        firstname,
        lastname,
        gender,
        level
    FROM staging_events
    where firstname is not null
)
"""

song_table_insert = """
INSERT INTO songs (
    song_id,
    title,
    artist_id,
    year,
    duration
) (
    SELECT
        song_id,
        title,
        artist_id,
        year,
        duration
    FROM staging_songs
)
"""

artist_table_insert = """
INSERT INTO artists (
    artist_id,
    name,
    location,
    latitude,
    longitude
) (
    SELECT
        artist_id,
        artist_name,
        artist_location,
        artist_latitude,
        artist_longitude
    FROM staging_songs
)
"""

time_table_insert = """
INSERT INTO time (
    start_time,
    hour,
    day,
    week,
    month,
    year,
    weekday
) (
    SELECT
        (timestamp 'epoch' + ts::numeric / 1000 * interval '1 second'),
        EXTRACT (HOUR FROM (timestamp 'epoch' + ts::numeric / 1000 * interval '1 second')),
        EXTRACT (DAY FROM (timestamp 'epoch' + ts::numeric / 1000 * interval '1 second')),
        EXTRACT (WEEK FROM (timestamp 'epoch' + ts::numeric / 1000 * interval '1 second')),
        EXTRACT (MONTH FROM (timestamp 'epoch' + ts::numeric / 1000 * interval '1 second')),
        EXTRACT (YEAR FROM (timestamp 'epoch' + ts::numeric / 1000 * interval '1 second')),
        EXTRACT (DAYOFWEEK FROM (timestamp 'epoch' + ts::numeric / 1000 * interval '1 second'))
    FROM staging_events
)
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
