from sqlalchemy import Column, Integer, BigInteger

from models.db.database import Database


class Stats(Database.base):
    __tablename__ = 'stats'

    id = Column(Integer, primary_key=True)
    discordUserId = Column(BigInteger, unique=True, nullable=False)
    quizzesTaken = Column(Integer, default=0)
    quizzesGottenCorrect = Column(Integer, default=0)
    gptApiCalls = Column(Integer, default=0)

    def __repr__(self):
        return (f"<Stats(id={self.id}, discordUserId={self.discordUserId}, "
                f"quizzesTaken={self.quizzesTaken}, quizzesGottenCorrect={self.quizzesGottenCorrect}, "
                f"gptApiCalls={self.gptApiCalls})>")

    @classmethod
    def insert(cls, discordUserId, quizzesTaken, quizzesGottenCorrect, gptApiCalls, session):
        new_stats = cls(discordUserId=discordUserId, quizzesTaken=quizzesTaken,
                        quizzesGottenCorrect=quizzesGottenCorrect, gptApiCalls=gptApiCalls)
        session.add(new_stats)
        session.commit()
        return new_stats

    @classmethod
    def get_from_user_id(cls, discordUserId, session):
        existing_stats = session.query(cls).filter_by(discordUserId=discordUserId).first()

        if existing_stats is None:
            cls.insert(discordUserId, 0, 0, 0, session)
            return cls.get_from_user_id(discordUserId, session)

        return existing_stats

