class Tracker:
    # Eric Poroznik

    """
    This is the tracker's class. This will be used to create trackers in the JSON file.
    
    Methods:
        create_tracker: creates a tracker and inserts it into the json file


    Attributes:
        num_trackers: int | Number of current trackers
        tracker_num: int | A tracker's ID so we can track the tracker
        course: string | Name of the assignment's course
        assignment_name: string | Name of the assignment
        due_date: string | Day it is due
        due_time: string | Time it is due, if none is provided it defaults to 23:59/11:59 PM of that day 

    """
    def __init__(self, num_trackers):
        self.num_trackers = num_trackers
        self.assignments_file = "data/assignments.json"

    @classmethod
    def create_tracker(self, course_name: str, assignment_name:str, due_date: str, due_time: str = None):
        """
        Create an assignment tracker in the assignments json file
        """
        
        # We will assume the due time is midnight, as this is the case with most assignments. 
        if due_time is None:
            due_time = "23:59"

        tracker_num = self.num_trackers + 1

    