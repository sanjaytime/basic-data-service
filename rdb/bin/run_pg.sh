#!/bin/bash
docker run --name postgres_db -e POSTGRES_PASSWORD=yourpassword -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres

