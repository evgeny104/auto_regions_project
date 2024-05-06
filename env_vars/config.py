import os
from dotenv import (
    load_dotenv)

load_dotenv()                                                   # loads environment variables from the .env file

URL = os.getenv('API_URL')                                      # To store global variables
print(f"Hello: {os.getenv('API_URL')}")
