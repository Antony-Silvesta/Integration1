from pymongo import MongoClient

# Connect to MongoDB on localhost
client = MongoClient("mongodb://localhost:27017/")

# Create or access a database
db = client["my_database"]  # Replace "my_database" with your desired database name

# Create a collection with an option to ensure creation
collection = db.create_collection("my_collection", capped=False)

# Print confirmation
print(f"Database '{db.name}' and Collection '{collection.name}' are created.")
