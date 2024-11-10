from sqlalchemy import Column, Integer, BigInteger

from models.db.database import Database


class Stats(Database.base):
    """
    A class for storing user statistics in the database as objects,
    and class methods performing CRUD (create-read-update-delete) operations on them

    Attributes:
        id (int): The unique identifier of the stats
        discordUserId (int): The Discord user ID of the user
        quizzesTaken (int): The number of quizzes taken by the user
        quizzesGottenCorrect (int): The number of quizzes the user has gotten correct
        gptApiCalls (int): The number of GPT API calls made by the user
    """
    __tablename__ = 'stats'

    id = Column(Integer, primary_key=True)
    discordUserId = Column(BigInteger, unique=True, nullable=False)
    quizzesTaken = Column(Integer, default=0)
    quizzesGottenCorrect = Column(Integer, default=0)
    gptApiCalls = Column(Integer, default=0)

    def __repr__(self):
        """
        String representation of a user's statistics

        :return: A string representation of the user's statistics
        """
        return (f"<Stats(id={self.id}, discordUserId={self.discordUserId}, "
                f"quizzesTaken={self.quizzesTaken}, quizzesGottenCorrect={self.quizzesGottenCorrect}, "
                f"gptApiCalls={self.gptApiCalls})>")

    @classmethod
    def insert(cls, discordUserId, quizzesTaken, quizzesGottenCorrect, gptApiCalls, session):
        """
        Insert a new user's statistics into the database

        :param discordUserId: The discord's user ID
        :param quizzesTaken: The number of quizzes taken by the user
        :param quizzesGottenCorrect: The number of quizzes the user has gotten correct
        :param gptApiCalls: The number of GPT API calls made by the user
        :param session: The database session

        :return: The newly created stats object
        """

        new_stats = cls(discordUserId=discordUserId, quizzesTaken=quizzesTaken,
                        quizzesGottenCorrect=quizzesGottenCorrect, gptApiCalls=gptApiCalls)
        session.add(new_stats)
        session.commit()
        return new_stats

    @classmethod
    def get_from_user_id(cls, discordUserId, session):
        """
        Get the user's statistics from the database by their Discord user ID

        :param discordUserId: The discord's user ID
        :param session: The database session

        :return: The user's statistics object, created if it doesn't already exist
        """

        existing_stats = session.query(cls).filter_by(discordUserId=discordUserId).first()

        if existing_stats is None:
            cls.insert(discordUserId, 0, 0, 0, session)
            return cls.get_from_user_id(discordUserId, session)

        return existing_stats

