FROM jupyter/pyspark-notebook

USER root

COPY script.py /home/



# Download and copy driver
RUN wget  https://jdbc.postgresql.org/download/postgresql-42.2.5.jar
RUN mv postgresql-42.2.5.jar /home/postgresql-42.2.5.jar

# Copy parquet files
COPY parquet/clicks.parquet.gzip /home/jovyan/clicks.parquet.gzip

ENV CLASSPATH="/home/"



CMD ["spark-submit", "--driver-class-path", "/home/postgresql-42.2.5.jar", "--jars", "/home/postgresql-42.2.5.jar", "/home/script.py"]
