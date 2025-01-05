import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
from typing import Generator

# Load environment variables
load_dotenv()

# Database credentials
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "movie_rez_db")
DB_USER = os.getenv("DB_USER", "ooghre")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# Database URL
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class
Base = declarative_base()

class DatabaseSession:
    def __init__(self):
        self._session: Session | None = None

    @property
    def session(self) -> Session:
        if self._session is None:
            self._session = SessionLocal()
        return self._session

    def close(self):
        if self._session:
            self._session.close()
            self._session = None

    def commit(self):
        if self._session:
            self._session.commit()

    def rollback(self):
        if self._session:
            self._session.rollback()

# Global database session instance
db = DatabaseSession()

@contextmanager
def get_db() -> Generator[Session, None, None]:
    """Context manager for database sessions"""
    try:
        yield db.session
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
