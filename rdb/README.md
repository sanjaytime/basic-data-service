# PySpark PostgreSQL Docker Pipeline Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Running the PostgreSQL Docker Container](#running-postgresql-docker-container)
4. [Running the PySpark Script](#running-pyspark-script)
5. [Verifying Parquet Files Load](#verifying-parquet-files-load)
6. [Potential Improvements](#potential-improvements)

## Introduction

This pipeline runs a PostgreSQL database inside a Docker container, populates the database with data, exports the data using PySpark and saves it as Parquet files.

## Requirements

- Docker
- PySpark
- Python 3.7+
- Access to a Unix-like shell (Bash, ZSH, etc.)

## Running the PostgreSQL Docker Container

1. Run the PostgreSQL Docker container with the following command:

    ```
    docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
    ```

   Replace `some-postgres` with your preferred container name and `mysecretpassword` with your preferred password.

2. To check that the container is running, use:

    ```
    docker ps
    ```

## Running the PySpark Script

1. Create a PySpark script (`your_script.py`) which connects to your PostgreSQL database and writes data into Parquet files.

2. Run the script with the following command:

    ```
    spark-submit --driver-class-path postgresql-42.2.14.jar --jars postgresql-42.2.14.jar your_script.py
    ```

   Replace `postgresql-42.2.14.jar` with the path to your PostgreSQL JDBC driver and `your_script.py` with the path to your script.

## Verifying Parquet Files Load

1. To check if the Parquet files have been loaded successfully, you can use PySpark to read the files:

    ```python
    from pyspark.sql import SparkSession

    spark = SparkSession.builder.getOrCreate()
    df = spark.read.parquet("/path/to/your/parquet/file")
    df.show()
    ```

   Replace `/path/to/your/parquet/file` with the path to your Parquet file. If the Parquet files have been loaded successfully, you should be able to see the data frame in the output.

## Potential Improvements

1. **Error Handling**: Add robust error handling and data validation to ensure the quality and consistency of data.
2. **Container Management**: Implement better Docker container management to handle startup and shutdown of the database automatically.
3. **Scaling**: Leverage distributed systems such as Hadoop or Kubernetes to enable this pipeline to process larger amounts of data.
4. **Security**: Enhance security measures, such as encrypting sensitive information and using secure connection methods.
5. **Testing**: Implement more comprehensive testing, especially integration and end-to-end tests to ensure the entire pipeline functions as expected.
6. **Logging and Monitoring**: Improve logging and add monitoring to track the system's health and data processing status. This can be helpful in debugging and improving system performance.
7. **Data Partitioning**: If dealing with big data, consider partitioning your
   Parquet files for more efficient data querying.

To log into the PostgreSQL shell for a running PostgreSQL docker container, you can use the `docker exec` command, which allows you to run commands in a running container. Here's how:

1. First, you need to find the name or ID of your running PostgreSQL Docker container. You can list all running containers with the command:

    ```bash
    docker ps
    ```

    Look for the container running PostgreSQL in the output of this command.

2. Once you have the container's ID or name, you can log into the PostgreSQL shell with the following command:

    ```bash
    docker exec -it <container-name-or-id> psql -U <username> -d <database-name>
    ```

    Replace `<container-name-or-id>` with the actual name or ID of your container, `<username>` with your PostgreSQL username, and `<database-name>` with the name of the database you want to connect to.

    If you used `postgres` as the username when setting up your PostgreSQL Docker container (which is the default username provided by the PostgreSQL Docker image), and you want to connect to the `postgres` database, your command would look like:

    ```bash
    docker exec -it <container-name-or-id> psql -U postgres -d postgres
    ```

3. When prompted, enter your PostgreSQL password.

This should give you a `psql` prompt where you can execute SQL commands on your PostgreSQL database. If the database you tried to connect to does not exist, you will see an error message.


--

Build the Docker image

To build the Docker image, run the following command in your terminal from the same directory as your Dockerfile:

bash

docker build -t my_spark_image .

    Run the Docker container

Now that the image is built, you can run a Docker container from it. Use the following command to do so:

bash

docker run -it --network="host" my_spark_image

Here we use --network="host" option to use the host's networking, allowing the Docker container to access the PostgreSQL database running on your local machine.

Please remember, the host machine in this context means the machine on which you're running Docker. If you're running Docker in a virtualized context (like Docker Desktop for Mac or Windows), localhost will refer to that virtual machine, not your physical machine. Adjust your database host configuration accordingly.

That's it! Your Python script with the Spark code will now be executed inside the Docker container when you run it.
