import disnake
from disnake.ext import commands
from datetime import datetime, timedelta

from management.tracker_manager import create

# Eric Poroznik

class AssignmentTracker(commands.Cog):
    """
    This class creates, displays and manages contents inside the assignments.json folder.

    """
    def __init__(self, bot):
        self.bot = bot
        


    """
    JSON Format:
    
    tracker_id: number <- private
    course: string
    assignment_name: string
    due_date: string
    due_time: optional string
    """

    @commands.slash_command(description="Add an assignment to the tracker")
    async def addtotracker(self, interaction: disnake.ApplicationCommandInteraction, course:str, name:str, duedate: str, duetime:str = None):
        """
        Adds an assignment to track to the assignments.json file.

        :param course: The name of the course the assignment belongs to
        :param name: The assignment's name
        :param duedate: The calendar date of the assignment's due date
        :param duetime: The 24hr format of the time the assignment is due
        """

    @commands.slash_command(description="Check for any active assignments due")
    async def viewtrackers(self, interaction: disnake.ApplicationCommandInteraction):
        """
        Sorts through all active assingments and puts them into an orderly list based on due date
        """

    @tasks.loop(minutes=1)
    async def checktracker(self):
        now = datetime.now()