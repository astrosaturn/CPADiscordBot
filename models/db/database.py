from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class Database:
    """
    A static class for managing the database

    Attributes:
        engine: The database engine
        base: The base class for declarative
    """
    engine = None
    base = declarative_base()

    @classmethod
    def create_engine(cls, db_url: str):
        """
        Create a database engine

        :param db_url: The database URL
        """
        cls.engine = create_engine(db_url, echo=True)

    @classmethod
    def create_session(cls):
        """
        Create a database session, ensure it is closed after use

        :return: The database session
        """
        session = sessionmaker(bind=cls.engine)
        return session()

