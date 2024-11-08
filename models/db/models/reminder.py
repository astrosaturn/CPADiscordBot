from sqlalchemy import Integer, Column, BigInteger, String
from sqlalchemy.orm import declarative_base, sessionmaker

from models.db import database


class Reminder(database.Database.base):
    """
    A class for storing reminders in the database as objects, and class methods performing CRUD (create-read-update-delete) operations on them

    Attributes:
        id (int): The unique identifier of the reminder
        discordUserId (int): The Discord user ID of the user who created the reminder
        channelId (int): The Discord channel ID of the channel where the reminder was created
        name (str): The name of the reminder
        dueDatetime (str): The due date and time of the reminder
        reminderTime (str): The time to remind the user of the reminder
    """
    __tablename__ = 'reminders'

    id = Column(Integer, primary_key=True)
    discordUserId = Column(BigInteger)
    channelId = Column(BigInteger)
    name = Column(String)
    dueDatetime = Column(String)
    reminderTime = Column(String)

    def __repr__(self):
        """
        String representation of the reminder

        :return: A string representation of the reminder
        """
        return f"<Reminder(id={self.id}, discordUserId={self.discordUserId}, channelId={self.channelId}, name={self.name}, dueDatetime={self.dueDatetime}, reminderTime={self.reminderTime})>"

    @classmethod
    def insert(cls, discordUserId, channelId, name, dueDatetime, reminderTime):
        """
        Insert a new reminder into the database

        :param discordUserId: The discord's user ID
        :param channelId: The discord's channel ID
        :param name: The name of the reminder
        :param dueDatetime: The due date and time of the reminder
        :param reminderTime: The time to remind the user of the reminder
        """

        reminder = cls(discordUserId=discordUserId, channelId=channelId, name=name, dueDatetime=dueDatetime, reminderTime=reminderTime)

        session = database.Database.create_session()
        session.add(reminder)
        session.commit()

        session.close()

    @classmethod
    def get_from_user_id(cls, discordUserId):
        """
        Get all reminders from a user ID

        :param discordUserId: The discord's user ID
        :return: A list of reminders from the user ID
        """
        session = database.Database.create_session()
        reminders = session.query(cls).filter_by(discordUserId=discordUserId).all()

        session.close()
        return reminders

    @classmethod
    def get_from_user_id_and_name(cls, discordUserId, name):
        """
        Get a reminder from a user ID and name

        :param discordUserId: The discord's user ID
        :param name: The name of the reminder
        :return: The reminder from the user ID and name
        """
        session = database.Database.create_session()
        reminder = session.query(cls).filter_by(discordUserId=discordUserId, name=name).first()

        session.close()
        return reminder

    @classmethod
    def delete(cls, discordUserId, name):
        """
        Delete a reminder from a user ID and name

        :param discordUserId: The discord's user ID
        :param name: The name of the reminder
        """
        reminder = cls.get_from_user_id_and_name(discordUserId, name)

        if reminder:
            session = database.Database.create_session()
            session.delete(reminder)
            session.commit()
            session.close()