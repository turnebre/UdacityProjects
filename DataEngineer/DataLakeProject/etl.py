import configparser
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import dayofweek, udf, monotonically_increasing_id
from pyspark.sql.functions import (
    year,
    month,
    dayofmonth,
    hour,
    weekofyear,
    from_unixtime,
)
from pyspark.sql.types import IntegerType, TimestampType


config = configparser.ConfigParser()
config.read("dl.cfg")

os.environ["AWS_ACCESS_KEY_ID"] = config["DataLake"]["AWS_ACCESS_KEY_ID"]
os.environ["AWS_SECRET_ACCESS_KEY"] = config["DataLake"]["AWS_SECRET_ACCESS_KEY"]


def create_spark_session():
    spark = (
        SparkSession.builder.config(
            "spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.2.0"
        )
        .config("spark.executor.memory", "4g")
        .getOrCreate()
    )
    return spark


def process_song_data(spark, input_data, output_data):
    """
    Processes song data in s3 and writes to another bucket.
    """
    # get filepath to song data file
    song_data = input_data + "song_data/*/*/*/*.json"

    # read song data file
    df = spark.read.json(
        song_data,
    )

    # extract columns to create songs table
    songs_table = (
        df.select("song_id", "title", "artist_id", "year", "duration")
        .dropna(subset=["song_id"])
        .dropDuplicates()
    )

    # write songs table to parquet files partitioned by year and artist
    songs_table.write.mode("overwrite").parquet(
        os.path.join(output_data, "songs"), partitionBy=["year", "artist_id"]
    )

    # extract columns to create artists table
    artists_table = (
        df.select(
            "artist_id",
            "artist_name",
            "artist_location",
            "artist_latitude",
            "artist_longitude",
        )
        .dropna(subset=["artist_id"])
        .dropDuplicates()
    )

    # write artists table to parquet files
    artists_table.write.mode("overwrite").parquet(os.path.join(output_data, "artists"))


def process_log_data(spark, input_data, output_data):
    """
    Processes log data from s3 bucket and writes it to another bucket.
    """
    # get filepath to log data file
    log_data = input_data + "log_data/*/*/*/*.json"

    # read log data file
    df = spark.read.json(
        log_data,
    )

    # filter by actions for song plays
    df = df.filter("page == 'NextSong'")

    # extract columns for users table
    users_table = (
        df.select("userId", "firstName", "lastName", "gender", "level")
        .dropna(subset=["userId"])
        .dropDuplicates()
    )

    # write users table to parquet files
    users_table.write.mode("overwrite").parquet(os.path.join(output_data, "users"))

    # create timestamp column from original timestamp column
    get_timestamp = udf(lambda x: x / 1000, IntegerType())
    df = df.withColumn("timestamp", get_timestamp("ts"))

    # create datetime column from original timestamp column
    get_datetime = udf(lambda x: from_unixtime(x), TimestampType())
    df = df.withColumn("start_time", get_datetime("timestamp"))

    # extract columns to create time table
    time_table = df.select(
        "start_time",
        hour("start_time").alias("hour"),
        dayofmonth("start_time").alias("day"),
        dayofweek("start_time").alias("weekday"),
        month("start_time").alias("month"),
        year("start_time").alias("year"),
        weekofyear("start_time").alias("week"),
    )

    # write time table to parquet files partitioned by year and month
    time_table.write.mode("overwrite").parquet(
        os.path.join(output_data, "artists"), partitionBy=["year", "month"]
    )

    # read in song data to use for songplays table
    song_df = spark.read.json(input_data + "song_data/*/*/*/*.json")

    # extract columns from joined song and log datasets to create songplays table
    songplays_table = (
        log_data.join(
            song_df,
            [df.song == song_df.title, df.artist == song_df.artist_name],
            how="left",
        )
        .withColumn("songplay_id", monotonically_increasing_id())
        .withColumn("year", year("start_time"))
        .withColumn("month", "start_time")
        .select(
            "songplay_id",
            "start_time",
            "user_id",
            "level",
            "song_id",
            "artist_id",
            "session_id",
            "location",
            "userAgent",
            "year",
            "month",
        )
    )

    # write songplays table to parquet files partitioned by year and month
    songplays_table.write.mode("overwrite").parquet(
        os.path.join(output_data, "song_plays"), partitionBy=["year", "month"]
    )


def main():
    """
    Calls above functions toread and write each dataset.
    """
    spark = create_spark_session()
    input_data = "s3a://udacity-dend/"
    output_data = "s3a://redhawks211/"
    print(spark.sparkContext.uiWebUrl)
    process_song_data(spark, input_data, output_data)
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()
