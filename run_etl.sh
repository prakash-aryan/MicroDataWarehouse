#!/bin/bash

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