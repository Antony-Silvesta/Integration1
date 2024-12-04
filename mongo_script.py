import os
from pymongo import MongoClient

def main():
    # Fetch MongoDB credentials from environment variables
    mongo_uri = os.getenv("MONGO_URI")
    db_name = os.getenv("MONGO_DB")

    # Ensure the environment variables are set
    if not mongo_uri or not db_name:
        raise EnvironmentError("MongoDB URI or Database Name is not set in environment variables.")

    # Connect to MongoDB
    print(f"Connecting to MongoDB at {mongo_uri}")
    client = MongoClient(mongo_uri)
    db = client[db_name]

    # Example: Fetch data from a collection
    collection = db["my_collection"]
    data = list(collection.find({}))  # Fetch all documents
    print("Fetched data from MongoDB collection:")
    print(data)

if __name__ == "__main__":
    main()
