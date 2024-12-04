from pymongo import MongoClient

# Define MONGO_URI in the global scope
MONGO_URI = "mongodb://localhost:27017"

def main():
    client = MongoClient(MONGO_URI)
    db = client['my_database']  # Replace with your DB name
    collection = db['my_collection']  # Replace with your collection name

    # Fetch all documents
    data = list(collection.find({}))
    print(data)

if __name__ == "__main__":
    print("Connecting to MongoDB at", MONGO_URI)
    main()
