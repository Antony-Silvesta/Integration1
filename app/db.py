from pymongo import MongoClient
import os

# MongoDB connection parameters
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "mydb"
COLLECTION_NAME = "test"

def connect_db():
    """Connect to MongoDB and return the database object."""
    try:
        client = MongoClient(MONGO_URI)
        print("Connected to MongoDB")
        return client[DB_NAME]  # Return the database object directly
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        exit(1)

def seed_database():
    """Access the database (no seed data to insert)."""
    db = connect_db()
    try:
        # Just print a success message to confirm the database connection
        print(f"Connected to collection '{COLLECTION_NAME}' in the '{DB_NAME}' database.")
    except Exception as e:
        print(f"Error accessing the database: {e}")

if __name__ == "__main__":
    seed_database()
