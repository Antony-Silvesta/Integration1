import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    mongo_uri = os.getenv("MONGO_URI")
    mongo_db = os.getenv("MONGO_DB")
    collection_name = "my_collection"

    if not mongo_uri or not mongo_db:
        raise ValueError("Environment variables MONGO_URI or MONGO_DB are not set.")

    print(f"Connecting to MongoDB at {mongo_uri}...")

    try:
        client = MongoClient(mongo_uri)
        db = client[mongo_db]
        collection = db[collection_name]

        data = list(collection.find({}))

        print(f"Documents in collection '{collection_name}':")
        for entry in data:
            print(entry)

    except Exception as e:
        print("Failed to connect or fetch data:", str(e))
        raise

if __name__ == "__main__":
    main()
