from models.db.database import *
from models.db.models.tracker import TrackerModel
from sqlalchemy.orm import Session


class Tracker:
    # Eric Poroznik

    """
    This is the tracker's class. This will be used to create trackers in the database .
    
    Methods:
        create_tracker: creates a tracker and inserts it into the database
        get_tracker_by_id: returns all of a tracker's data from an id
        delete_tracker: deletes a tracker from a given id

    Attributes:
        course: string | Name of the assignment's course
        assignment_name: string | Name of the assignment
        due_date: string | Day it is due
        due_time: string | Time it is due, if none is provided it defaults to 23:59/11:59 PM of that day 

    """

    @classmethod
    def create_tracker(self, i_course_name:str, i_assignment_name:str, i_due_date: str, i_due_time: str = None):
        """
        Create an assignment tracker in the database

        :attribute course_name: Name of the course
        :attribute assignment_name: Name of the assignment
        :attribute due_date: The date the assignment is due
        :attribute due_time: The time its due at (If none, defaults to 23:59)
        """
    

        # Now create a session for the database.
        session = Database.create_session()
        try:
            TrackerModel.insert(i_course_name, i_assignment_name, i_due_date, i_due_time, session)
            session.commit()
            print(f"Tracker successfully created for: {i_course_name}, {i_assignment_name} due on {i_due_date} at {i_due_time}")
        except Exception as e:
            session.rollback()
            print(f"OOPS! Database fucky wucky {e}")
        finally:
            session.close()
        
    @classmethod
    def show_trackers(self):
        """
        Retrieves 10 trackers from the DB in order of due date
        """
        session = Database.create_session()
        active_trackers = TrackerModel.get_trackers(session)
        session.commit()
        session.close()

        return active_trackers
        
    @classmethod
    def get_tracker_by_id(self, tracker_id: int) -> dict | None:
        try:
            session = Database.create_session()
            tracker_info = session.get(TrackerModel, tracker_id)

            print(f"Query result for tracker_id {tracker_id}: {tracker_info}")

            if tracker_info: # If we successfully find a tracker with this id, execute
                data = {
                    "id": tracker_info.id,
                    "course": tracker_info.course,
                    "assignment_name": tracker_info.assignment_name,
                    "due_date": tracker_info.due_date,
                    "due_time": tracker_info.due_time
                }
                return data
            else:
                return None
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


    