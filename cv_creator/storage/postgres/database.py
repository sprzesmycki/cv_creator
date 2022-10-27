from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from cv_creator.config import config

SQLALCHEMY_DATABASE_URI = config.get("POSTGRES_DB_URI")

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
