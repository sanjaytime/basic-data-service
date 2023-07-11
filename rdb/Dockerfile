FROM jupyter/pyspark-notebook

USER root

# Copy JDBC Driver into the image
#COPY postgresql-42.6.0.jar /home/jovyan/driver/postgresql-42.6.0.jar
COPY postgresql-42.6.0.jar /home/

# Add the JDBC driver to the classpath
ENV SPARK_CLASSPATH=/home/postgresql-42.2.5.jar



# Copy spark script
COPY script.py /home/


# Copy parquet files
COPY parquet/clicks.parquet.gzip /home/jovyan/clicks.parquet.gzip




CMD ["spark-submit", "/home/script.py"]

