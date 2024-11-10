from sqlalchemy import Column, Integer, String

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
        
        """
        tracker_info = self( course=course,
                            assignment_name = assignment_name, due_date=due_date, 
                            due_time = due_time)
        
        session.add(tracker_info)
        session.commit()

        return tracker_info
    
    @classmethod
    def remove(cls, id, session):
        tracker_info = session.query(cls).filter_by(id=id).first()
        
        if tracker_info:
            session.delete(tracker_info)
            session.commit()
            return True
        else:
            return False