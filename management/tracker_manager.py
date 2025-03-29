from models.db.database import *
from models.db.models.trackerModel import TrackerModel


class Tracker:
    # Eric Poroznik

    """
    This is the tracker's class. This will be used to create trackers in the database .
    
    Methods:
        create_tracker: creates a tracker and inserts it into the database
        get_tracker_by_id: returns all of a tracker's data from an id
        delete_tracker: deletes a tracker from a given id
        show_tracker: Gets 10 trackers in order of due date.

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
        try:
            TrackerModel.insert(i_course_name, i_assignment_name, i_due_date, i_due_time)
            print(f"Tracker successfully created for: {i_course_name}, {i_assignment_name} due on {i_due_date} at {i_due_time}")
        except Exception as e:
            print(f"OOPS! Database fucky wucky {e}")
        
    @classmethod
    def show_trackers(self):
        """
        Retrieves 10 trackers from the DB in order of due date
        """
        active_trackers = TrackerModel.get_trackers()

        return active_trackers
        
    @classmethod
    def get_tracker_by_id(self, tracker_id: int):
        try:
            tracker = TrackerModel.get_tracker(tracker_id)
            if tracker:
                return tracker
            else:
                print(f"Tracker with ID {tracker_id} not found.")
                return None
        except Exception as e:
            print(f"OOPS! There was an issue getting a tracker: {e}")
            return None


    @classmethod
    def delete_tracker(self, tracker_id:int):
        """
        Delete an assignment tracker in the database

        :attribute tracker_id: Takes a tracker_id and deletes the tracker where the id is.
        """
        try:
            TrackerModel.remove(tracker_id)
        except Exception as e:
            print(f"OOPS! Database fucky wucky {e}")


    