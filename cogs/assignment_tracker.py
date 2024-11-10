import disnake, json
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
    async def addtotracker(self, interaction: disnake.ApplicationCommandInteraction,
                           assign_name: str, i_date: str, i_time:str = None):
        """
        Adds an assignment to track to the database

        :param course: The name of the course the assignment belongs to
        :param name: The assignment's name
        :param due_date: The calendar date of the assignment's due date
        :param due_time: The 24hr format of the time the assignment is due
        """
        with open('data/courses.json', 'r') as file:
            data = json.load(file)

        course_list = data.get('course', [])

        courses = disnake.ui.StringSelect(
            custom_id="tracker_course",
            placeholder="Select a course",
            options=course_list
        )

        # Create these global variables so we can use them in both methods, "i" means initial
        global assignment_name, date, time

        assignment_name = assign_name
        date = i_date
        # Assign the time to midnight if no time is provided
        time = i_time if  i_time is not None else "23:59"

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

        chosen_course = interaction.values[0] # Choose the first chosen result

        # In my opinion, Embeds just look better so lets use an embed here!
        # -------------------------------------------------------------------------
        #Initialize the basic attributes of the embed, and create the object.
        embed = disnake.Embed(
            title=f"Assignment Tracker successfully created!",
            description=f"{next(iter(interaction.values))}", # this is stupid
            color=disnake.Color.green(),
            timestamp=datetime.now()
        )
        #Add the name of the author to the embed, this will just be the user who created it
        embed.set_author(
            name = interaction.user.name,
            icon_url = interaction.user.avatar.url
        ) 
        
        #Use the alarm clock image, because why not?
        embed.set_image(url="https://cdn3.iconfinder.com/data/icons/simple-microphone-icon/512/Clock_Icon-3-512.png") 


        embed.add_field(name="Assignment Name", value=f"{assignment_name}", inline = True)
        embed.add_field(name="Due Date", value=f"{date}", inline = True)
        embed.add_field(name="Due Time", value=f"{time}", inline = True)

        #Now, we insert the tracker into the database by sending the data we just created and respond with a success message.
        try:
            Tracker.create_tracker(str(chosen_course), assignment_name, date, time)
            await interaction.response.edit_message("",embed=embed)
        except Exception as e: # Or an error message.
            await interaction.response.send_message(embed=disnake.Embed(title="There was an exception:", description=e, 
                                                                                color=disnake.Color.red()), ephemeral=True)


    
    @commands.slash_command(description="Check for any active assignments due")
    async def viewtrackers(self, interaction: disnake.ApplicationCommandInteraction):
        """
        Sorts through all active assignments and puts them into an orderly list based on due date

        """

    @commands.slash_command(description="Deletes a tracker based on ID")
    async def deletetracker(self, interaction: disnake.ApplicationCommandInteraction, tracker_id: int):
        """
        Takes a tracker ID, sorts through the database using the ID, and deletes the associated tracker.
        
        :assign interaction: The interaction object
        :assign tracker_id: The tracker's ID that we will use to delete it
        """
        if tracker_id < 0 or tracker_id is None:
            await interaction.response.send_message("Tracker ID is invalid! Please input a valid number!", ephemeral=True)


        # Now, lets attempt to delete the tracker
        try:
            Tracker.delete_tracker(tracker_id)
            await interaction.response.send_message("Tracker successfully deleted")
        except Exception as e:
            await interaction.response.send_message(f"There was an exception! {e}", ephemeral=True)
        

    @tasks.loop(minutes=1)
    async def checktracker(self):
        now = datetime.now()

def setup(bot):
    bot.add_cog(AssignmentTracker(bot))