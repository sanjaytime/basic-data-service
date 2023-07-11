from pyspark.sql import SparkSession

# Create a spark session
spark = SparkSession.builder \
    .appName('Parquet to DB') \
    .getOrCreate()

# Read the parquet file
df = spark.read.parquet('clicks.parquet.gzip')

# Set the properties for PostgreSQL
properties = {
    "user": "postgres",
    "password": "yourpassword",
    "driver": "org.postgresql.Driver"
}

# Write the DataFrame to PostgreSQL table "items"
df.write.jdbc(url="jdbc:postgresql://host.docker.internal:5432/postgres_db", table="items", mode="append", properties=properties)

spark.stop()

