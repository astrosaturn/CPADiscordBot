# Weekly recap written and developed by Hannah Alkenbrack <3

# Import the disnake library to interact with the Discord API.
# disnake is a Python library that allows us to create Discord bots.
import disnake
# Import necessary modules from disnake for commands and scheduled tasks.
from disnake.ext import commands, tasks
# Import the datetime module to handle dates and times (for scheduling weekly tasks).
import datetime

# Define a class to handle all the weekly recap-related commands and actions.
class weeklyRecapCommand(commands.Cog):
    """
    This class contains all the commands and tasks related to weekly recaps.
    It will allow users to update recaps for specific courses and will send
    weekly updates automatically.
    """

    def __init__(self, bot):
        """
        Initializes the cog (module) for managing weekly recaps.
        
        Parameters:
        - bot: This is the bot instance that this cog is attached to. It allows the cog 
          to interact with the bot and the Discord API.
        """
        self.bot = bot  # Store the bot instance to be able to interact with Discord later.
        
        # Dictionary that stores recaps for each course. The keys are course names, 
        # and the values are the recap messages.
        self.recap_data = {
            "Care 10": "No updates; always set to BS.",  
            "COMP 333": "No recap added yet.",  
            "COMP 1081": "No recap added yet.",  
            "COMP 220": "No recap added yet.",  
            "COMP 206": "No recap added yet."   
        }
        
        # List to store weekly update contributions. Users can contribute updates here.
        self.weekly_contributions = []

        # Start the background task that will send weekly recaps at the scheduled time.
        # This task will run automatically when the cog is loaded.
        self.weekly_recap_task.start()

    @commands.slash_command(description="Add or update the weekly recap for a course.")
    async def add_recap(self, inter: disnake.ApplicationCommandInteraction, course: str, recap: str):
        """
        This is a slash command that allows users to add or update the recap for a given course.
        
        Parameters:
        - inter: The interaction that triggered this command, used to send a response back to the user.
        - course: The name of the course for which the recap should be added or updated.
        - recap: The new recap message to be stored for the specified course.
        """
        
        # Check if the provided course exists in our recap_data dictionary.
        if course in self.recap_data:
            # If the course exists, update its recap with the new message.
            self.recap_data[course] = recap  
            # Send a confirmation message back to the user indicating the recap was updated.
            self.weekly_contributions.append(f"{course}: {recap}")
            await inter.response.send_message(f"Weekly recap for {course} updated!")
        else:
            # If the course is not found in the dictionary, inform the user.
            await inter.response.send_message(f"Course '{course}' not found. Please enter a valid course.")

   
    @tasks.loop(hours=168)  # This task runs every 168 hours, which is equivalent to one week.
    async def weekly_recap_task(self):
        """
        This task sends out the weekly recap every Sunday at a specific time (9 AM in this case).
        It will iterate through the courses and send the recap for each one.
        """
        # Get the current time in UTC
        now = datetime.datetime.utcnow()

        # Check if it's Sunday at 9 AM (or any other time you want to send weekly recaps)
        if now.weekday() == 6 and now.hour == 9:  # Weekday 6 is Sunday, and 9 is 9 AM.
            channel = self.bot.get_channel(1304148534114914364)  # hardcoded channel ID  for channel ID (NEED TO CHANGE LATER MAYBE TO MANUALLY ENTER INSTEAD OF HARDCODED).
            recap_message = "Here are the weekly recaps:\n"
            
            # Iterate over all courses and their recaps, appending them to the message.
            for course, recap in self.recap_data.items():
                recap_message += f"\n{course}: {recap}"
            
            # Send the message to the specified channel
            await channel.send(recap_message)
            
            print("Weekly recap sent!")
    
    

    #Write a list function for all current contributions
    @commands.slash_command(description="lists all current recap content")
    async def weekly_recap_list(self, inter: disnake.ApplicationCommandInteraction):
        recap_list_msg = ""
        for contribution in self.weekly_contributions:
            recap_list_msg += contribution + "\n"
        
        await inter.response.send_message("Here is the weekly recap list:\n\n" + recap_list_msg)

        
def setup(bot):
    bot.add_cog(weeklyRecapCommand(bot))


