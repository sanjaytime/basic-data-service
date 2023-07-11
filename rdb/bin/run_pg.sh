#!/bin/bash
docker run --name postgres_db -e POSTGRES_PASSWORD=yourpassword -p 5432:5432 -d postgres

