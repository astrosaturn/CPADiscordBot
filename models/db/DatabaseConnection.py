import sqlite3, os

from dotenv import load_dotenv

load_dotenv()

class DatabaseConnection:
    """
    Class to manage connection to the SQLite database.

    In Java we handled this through a singleton but python is messy
    with that kind of stuff so I'm not gonna do all that.

    From Eric:
    I dont like SQLAlchemy so I'm not using it. 
    I also don't like the ORM style of SQLAlchemy. I prefer to write my own queries and have more control over the database interactions.
    """
    def __init__(self):
        self.conn = sqlite3.connect("./data/database.sqlite")
        self.cursor = self.conn.cursor()

    """
    def conn():
        try:
            conn = sqlite3.connect("sqlite:///data/database.sqlite")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            conn = None
        finally:
            return conn
        
    def cursor():
        try:
            cursor = conn.cursor()
        except sqlite3.Error as e:
            print(f"Error creating cursor: {e}")
            cursor = None
        finally:
            return cursor
    """