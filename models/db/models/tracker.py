from sqlalchemy import Column, Integer, String, func

from models.db.database import Database

# Eric Poroznik
class TrackerModel(Database.base):
    """
    A class for displaying, removing, and adding trackers to and from the database.
    
    Attributes:
        id (int): Special identifier of each tracker  [Auto Increments, Not NULL] (Primary Key) 
        course (string): The name of the course the tracker belongs to [Not NULL]
        assignment_name (string): The name of the assignment [Not NULL]
        due_date (string): The date the assignment is due DD-MM-YYYY [Not NULL]
        due_time (string): The time the assignment is due HH:MM [Not null]
    """

    # Define the table and the columns
    __tablename__ = 'trackers'
    id = Column(Integer, primary_key = True, autoincrement=True)
    course = Column(String, nullable=False)
    assignment_name = Column(String, nullable=False)
    due_date = Column(String, nullable=False)
    due_time = Column(String, nullable=False)

    @classmethod
    def insert(self, course, assignment_name,
                    due_date, due_time, session):
        """
        Inserts a new tracker into the database

        :param course: The course name
        :param assignment_name: The assignment's name
        :param due_date: The day the assignment is due [DD-MM-YYYY]
        :param due_time: The time the assignment is due [HH:MM]
        """

        #Build a list for the tracker
        tracker_info = self( course=course,
                            assignment_name = assignment_name, due_date=due_date, 
                            due_time = due_time)
        
        # Add it to the table
        session.add(tracker_info)
        session.commit()

        # Return what we added for debugging purposes
        return tracker_info
    
    @classmethod
    def remove(self, id, session):
        """
        Removes a tracker from the database by ID

        :param id: The tracker's id 
        :param session: The current database's session
        """

        # Get the tracker and where it is
        tracker_info = session.query(self).filter_by(id=id).first()
        
        # If we successfully got the tracker,
        if tracker_info:
            # Delete the tracker
            session.delete(tracker_info)
            session.commit()
            return True
        else:
            # Return false.
            return False
        
    @classmethod
    def get_trackers(self, session):
        """
        Gets 10 trackers that are ordered by due date

        :returns: List of 10 trackers
        """
        # Get the top 10 trackers ordered by due_date
        results = session.query(TrackerModel).order_by(
            func.strftime('%Y-%m-%d', TrackerModel.due_date)
        ).limit(10).all()

        #TODO: bash my head against a wall
        for record in results:
            pass
        print(f"RESULTS:  {results}")
    