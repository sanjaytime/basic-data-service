from pyspark.sql import SparkSession

# Create a spark session
spark = SparkSession.builder \
    .appName('Parquet to DB') \
    .config("spark.jars", "/home/postgresql-42.2.5.jar") \
    .config("spark.driver.extraClassPath", "/home/postgresql-42.2.5.jar") \
    .config("spark.executor.extraClassPath", "/home/postgresql-42.2.5.jar")\
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
df.write.jdbc(url="jdbc:postgresql://host.docker.internal:5432/mydatabase", table="items", mode="append", properties=properties)

spark.stop()

