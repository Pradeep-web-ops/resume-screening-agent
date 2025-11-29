from tinydb import TinyDB, Query
from datetime import datetime
import os

class LocalDB:
    def __init__(self, db_path="data/db.json"):
        # Ensure data folder exists
        os.makedirs("data", exist_ok=True)

        self.db = TinyDB(db_path)
        self.table = self.db.table("results")

    def save(self, record: dict):
        """Save one resume screening result into TinyDB"""

        record["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.table.insert(record)

    def get_all(self):
        """Return all stored resume results"""
        return self.table.all()

    def search_by_name(self, resume_name):
        """Search results by resume name"""
        Q = Query()
        return self.table.search(Q.resume == resume_name)
