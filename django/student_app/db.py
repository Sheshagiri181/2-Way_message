import os
from pymongo import MongoClient

def get_db():
    # Use environment variables for credentials
    mongo_uri = os.getenv('MONGO_URI', '...............')
    try:
        client = MongoClient(mongo_uri)
        students = client['aagama_pr_1']['student']
        return students
    except Exception as e:
        print(f"Database connection error: {e}")
        return None
