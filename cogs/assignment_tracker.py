import disnake
from disnake.ext import commands, tasks
from datetime import datetime, timedelta

from management.tracker_manager import Tracker
from models.db.database import *
# Eric Poroznik

class AssignmentTracker(commands.Cog):
    """
    This class creates, displays and manages contents inside the database folder.

    :attribute assignment_name: The name of the assignment to track
    :attribute date: The due date of the assignment 
    """
    def __init__(self, bot):
        self.bot = bot


    """
    Format:
    
    tracker_id: number <- private
    course: string
    assignment_name: string
    due_date: string
    due_time: optional string
    """
    ##course:str, name:str, duedate: str, duetime:str = None):


    @commands.slash_command(description="Add an assignment to the tracker")
    async def addtotracker(self, interaction: disnake.ApplicationCommandInteraction, assign_name: str, i_date: str, i_time:str = None):
        """
        Adds an assignment to track to the database

        :param course: The name of the course the assignment belongs to
        :param name: The assignment's name
        :param due_date: The calendar date of the assignment's due date
        :param due_time: The 24hr format of the time the assignment is due
        """
        courses = disnake.ui.StringSelect(
            custom_id="tracker_course",
            placeholder="Select a course",
            options=["COMP1081", "COMP333", "COMP220", "COMP206"]
        )

        # Create these global variables so we can use them in both methods, "i" means initial
        global assignment_name, date, time

        assignment_name = assign_name
        date = i_date
        time = i_time

        await interaction.response.send_message("Pick a course for the tracker: ", components=[courses] )

    @commands.Cog.listener("on_dropdown")
    async def build_tracker(self, interaction: disnake.MessageInteraction):
        """
        Listener for the dropdown menu
        
        :param interaction: The object chosen from the dropdown menu
        """
        # If for some reason, or somehow, the drop down menu gives us the wrong component, we want to exit early.
        if interaction.component.custom_id != "tracker_course":
            return
        
        chosen_course = interaction.values[0] # Chose the first chosen result

        await interaction.response.send_message(f"{chosen_course} {assignment_name} {date}")
        try:
            Tracker.create_tracker(str(chosen_course), assignment_name, date, time)
        except Exception as e:
            print(f"FUCK. {e}")


    
    @commands.slash_command(description="Check for any active assignments due")
    async def viewtrackers(self, interaction: disnake.ApplicationCommandInteraction):
        """
        Sorts through all active assignments and puts them into an orderly list based on due date

        """

    @tasks.loop(minutes=1)
    async def checktracker(self):
        now = datetime.now()

def setup(bot):
    bot.add_cog(AssignmentTracker(bot))