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
