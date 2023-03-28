from dotenv import dotenv_values

config = dotenv_values("../.env")

POSTGRES_DB_URI = config.get("POSTGRES_DB_URI")
DEBUG = config.get("DEBUG")
