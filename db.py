# db.py
import os
from pymongo import MongoClient

def connect_db():
    """Establishes and returns a MongoDB connection."""
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")  # Default URI for local MongoDB
    MONGO_DB = os.getenv("MONGO_DB", "my_database")  # Default database name
    
    # Create a MongoDB client and connect to the specified database
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB]
    return db
