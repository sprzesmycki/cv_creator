from dotenv import dotenv_values
from pathlib import Path

config = dotenv_values(Path(__file__).resolve().parent.parent / '.env')

POSTGRES_DB_URI = config.get("POSTGRES_DB_URI")
DEBUG = config.get("DEBUG")
