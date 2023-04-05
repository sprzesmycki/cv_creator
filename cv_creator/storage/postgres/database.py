from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from cv_creator.config import POSTGRES_DB_URI

engine = create_engine(POSTGRES_DB_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
