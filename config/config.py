import os
from dotenv import load_dotenv
import os

load_dotenv()

sqlite_url = os.getenv("SQLITE_URL")

mongodb_url = os.getenv("MONGODB_URL")
mongodb_db = os.getenv("MONGODB_DB")
