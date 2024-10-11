#!/usr/bin/env python3
"""log stats from collection
"""
from pymongo import MongoClient

# Connect to MongoDB (adjust connection string as needed)
client = MongoClient("mongodb://localhost:27017/")

# Access the database and collection
db = client["logs"]
collection = db["nginx"]

# Total number of logs
log_count = collection.count_documents({})

# HTTP methods to check
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

# Count for each method
method_counts = {
    method: collection.count_documents({"method": method}) for method in methods
}

# Count documents with method GET and path /status
status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

# Output format as per the example
print(f"{log_count} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{status_check_count} status check")
