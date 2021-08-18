# DROP TABLES

songplay_table_drop = "drop table if exists songplays;"
user_table_drop = "drop table if exists users;"
song_table_drop = "drop table if exists songs;"
artist_table_drop = "drop table if exists artists;"
time_table_drop = "drop table if exists time;"

# CREATE TABLES

songplay_table_create = """
create table if not exists songplays 
    (songplay_id serial primary key,
    start_time timestamp not null, 
    user_id int not null,
    level text not null,
    song_id text, 
    artist_id text,
    session_id int not null,
    location text not null, 
    user_agent text not null);
"""

user_table_create = """
create table if not exists users
    (user_id int primary key,
    first_name text not null,
    last_name text not null,
    gender text not null,
    level text not null);
"""

song_table_create = """
create table if not exists songs
    (song_id text primary key,
    title text not null,
    artist_id text not null,
    year int not null,
    duration float not null);
"""

artist_table_create = """
create table if not exists artists
    (artist_id text primary key,
    name text not null,
    location text not null,
    latitude decimal,
    longitude decimal);
"""

time_table_create = """
create table if not exists time
    (start_time timestamp not null,
    hour int not null,
    day int not null,
    week int not null,
    month int not null,
    year int not null,
    weekday int not null);
"""

# INSERT RECORDS

songplay_table_insert = """
INSERT INTO songplays VALUES (default, %s, %s, %s, %s, %s, %s, %s, %s)
"""

user_table_insert = """
INSERT INTO users VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
"""

song_table_insert = """
INSERT INTO songs VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING
"""

artist_table_insert = """
INSERT INTO artists VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING
"""

time_table_insert = """
INSERT INTO time VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

# FIND SONGS

song_select = """
select song_id, a.artist_id
from songs a
left join artists b
on a.artist_id = b.artist_id
where %s = a.title
and %s = b.name
and %s = duration;
"""

# QUERY LISTS

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]

