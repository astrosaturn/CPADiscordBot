from models.db.DatabaseConnection import DatabaseConnection
import sqlite3

# Eric Poroznik
class TrackerModel(DatabaseConnection):
    """
    A class for displaying, removing, and adding trackers to and from the database.
    
    Attributes:
        id (int): Special identifier of each tracker  [Auto Increments, Not NULL] (Primary Key) 
        course (string): The name of the course the tracker belongs to [Not NULL]
        assignment_name (string): The name of the assignment [Not NULL]
        due_date (string): The date the assignment is due DD-MM-YYYY [Not NULL]
        due_time (string): The time the assignment is due HH:MM [Not null]
    """
    db_connection = DatabaseConnection()
    
    conn = db_connection.conn #Connection
    cursor = db_connection.cursor #Cursor, lets us execute queries

    try:
        #Create the table if it doesn't already exist.
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS trackers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    course TEXT NOT NULL,
                    assignment_name TEXT NOT NULL,
                    due_date TEXT NOT NULL,
                    due_time TEXT NOT NULL
                    )
                    ''')
    except sqlite3.Error as e:
        print(f"Error creating table: {e}") 

    @classmethod
    def get_tracker(self, id: int):
        """
        Gets a tracker by ID

        :param id: The tracker's id 
        """
        if id is None:
            raise ValueError("ID must be provided.")

        query = "SELECT * FROM trackers WHERE id = ?"
        try:
            # Execute the query and fetch the result
            self.cursor.execute(query, (id,))
            tracker = self.cursor.fetchone()
            return tracker
        
        except sqlite3.Error as e:
            print(f"Error fetching tracker: {e}")
            return None


    @classmethod
    def insert(self, course: str, assignment_name: str,
                    due_date: str, due_time: str):
        """
        Inserts a new tracker into the database

        :param course: The course name
        :param assignment_name: The assignment's name
        :param due_date: The day the assignment is due [DD-MM-YYYY]
        :param due_time: The time the assignment is due [HH:MM]
        """
        values = (course, assignment_name, due_date, due_time)
        for value in values:
            if not value:
                raise ValueError("All fields must be filled out.")

        query = "INSERT INTO trackers (course, assignment_name, due_date, due_time) VALUES (?, ?, ?, ?)"
        try:
            # Execute the query and commit the changes
            self.cursor.execute(query, values)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting tracker: {e}")

        # Return what we added for debugging purposes
        return values
    
    @classmethod
    def remove(self, id):
        """
        Removes a tracker from the database by ID

        :param id: The tracker's id 
        :param session: The current database's session
        """
        if not id:
            raise ValueError("ID must be provided.")
        
        query = "DELETE FROM trackers WHERE id = ?"
        try:
            # Execute the query and commit the changes
            self.cursor.execute(query, (id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error removing tracker: {e}")
            return False
        
    @classmethod
    def get_trackers(self):
        """
        Gets 10 trackers that are ordered by due date

        :returns: List of 10 trackers
        """
        query = "SELECT * FROM trackers ORDER BY due_date ASC LIMIT 10"
        try:
            # Execute the query and fetch the results
            self.cursor.execute(query)
            trackers = self.cursor.fetchall()
            return trackers
        except sqlite3.Error as e:
            print(f"Error fetching trackers: {e}")
            return []
    