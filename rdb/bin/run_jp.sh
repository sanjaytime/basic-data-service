#!/bin/bash
docker run --name jupyter_pyspark -e POSTGRES_PASSWORD=you:wqrpassword -p 5432:5432 -d postgres

