#!/bin/bash

# Set environment variables
export SPARK_HOME="/usr/lib/python3.11/site-packages/pyspark"
export PYTHONPATH="$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9.7-src.zip:$PYTHONPATH"

# Execute data.py script
echo "Executing data.py script..."
python3 data.py
echo "Database created successfully!"
echo "------------------------"

# Execute etl.py script
echo "Executing etl.py script..."
echo "------------------------"
python3 etl.py
echo "ETL process completed."
echo "------------------------"

# Start Metabase server
echo "Starting Metabase server..."
java -jar metabase.jar &
echo "Metabase server is running at http://localhost:3000"