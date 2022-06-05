
from dotenv import load_dotenv
import os

load_dotenv()


# mongodb
mongodb_url = os.getenv("MONGODB_URL")
mongodb_db = os.getenv("MONGODB_DB")


# security
secret_key = os.getenv("TOKEN_SECRET_KEY")
algorithm = os.getenv("TOKEN_ALGORITHM")
expire_time = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
