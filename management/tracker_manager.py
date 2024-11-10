from models.db.database import *
from models.db.models.tracker import TrackerModel


class Tracker:
    # Eric Poroznik

    """
    This is the tracker's class. This will be used to create trackers in the database .
    
    Methods:
        create_tracker: creates a tracker and inserts it into the database


    Attributes:
        no_trackers: int | Number of current trackers
        tracker_num: int | A tracker's ID so we can track the tracker
        course: string | Name of the assignment's course
        assignment_name: string | Name of the assignment
        due_date: string | Day it is due
        due_time: string | Time it is due, if none is provided it defaults to 23:59/11:59 PM of that day 

    """



    no_trackers = 0
    @classmethod
    def create_tracker(self, i_course_name:str, i_assignment_name:str, i_due_date: str, i_due_time: str = None):
        """
        Create an assignment tracker in the database

        :attribute course_name: Name of the course
        :attribute assignment_name: Name of the assignment
        :attribute due_date: The date the assignment is due
        :attribute due_time: The time its due at (If none, defaults to 23:59)
        """
    
        # Create a tracker number by increasing the current tracker number by one.
        self.no_trackers += 1
        tracker_id = self.no_trackers

        # Now create a session for the database.
        session = Database.create_session()
        try:
            TrackerModel.insert(tracker_id, i_course_name, i_assignment_name, i_due_date, i_due_time, session)
            session.commit()
            print(f"Tracker successfully created for: \nAssignment #{tracker_id} for course {i_course_name}, {i_assignment_name} due on {i_due_date} at {i_due_time}")
        except Exception as e:
            session.rollback()
            print(f"OOPS! Database fucky wucky {e}")
        finally:
            session.close()
        

    
    @classmethod
    def delete_tracker(self, tracker_id:int):
        """
        Delete an assignment tracker in the database

        :attribute tracker_id: Takes a tracker_id and deletes the tracker where the id is.
        """
        session = Database.create_session()
        try:
            TrackerModel.remove(tracker_id, session)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"OOPS! Database fucky wucky {e}")
        finally:
            session.close()


    