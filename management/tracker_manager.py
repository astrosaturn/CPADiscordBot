from models.db.database import *


class Tracker:
    # Eric Poroznik

    """
    This is the tracker's class. This will be used to create trackers in the JSON file.
    
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
    def create_tracker(self, course_name:str, assignment_name:str, due_date: str, due_time: str = None):
        """
        Create an assignment tracker in the database

        :attribute course_name: Name of the course
        :attribute assignment_name: Name of the assignment
        :attribute due_date: The date the assignment is due
        :attribute due_time: The time its due at (If none, defaults to 23:59)
        """
        
        # We will assume the due time is midnight, as this is the case with most assignments. 
        if due_time is None:
            due_time = "23:59"

        self.no_trackers += 1
        tracker_num = self.no_trackers


        print(f"Assignment #{tracker_num} for course {course_name}, {assignment_name} due on {due_date} at {due_time}")



    