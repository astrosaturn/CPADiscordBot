import disnake
from disnake.ext import commands

#Progress alert written by Tyler Moore
#This when used should report every assignemnt and test left unfinished by the user

"""
 Planning to use a database with ids to display both the course and assignment/test that is unfinished. 
 Needs 2 tables course table, assignment table.
 Course table should have only Id and course_name. Assignment table should have Id, course_id, assingment_name, boolean 1 if finished 0 if not.
 Add it so the user can select course to display unfinished work.
 """

class ProgressCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.progress_report = []
        #array data placeholders (going to use actually tables from database)
        self.course_table = [
            {"id": "1", "course_name": "COMP 333"}
        ]

        self.assignment_table = [
            {"id": "1", "course_id": "1", "assignment_name": "assignment1", "is_finished": "0"},
            {"id": "2", "course_id": "1", "assignment_name": "assignment2", "is_finished": "0"},
            {"id": "3", "course_id": "1", "assignment_name": "assignment3", "is_finished": "1"}
        ]

    @commands.slash_command(description="Displays unfinished work from all courses")
    async def progress_alert(self, inter: disnake.ApplicationCommandInteraction):
        #checks the courses one by one and sets course_id and course_name variables for later use when checking the assignments for that course
       for course in self.course_table:
        course_id = course["id"]
        course_name = course["course_name"]
       
        #Appends to progress_report the course name and its unfinsihed assignments
        #Checks every assignment in the table that has the same course_id and checks if its not finsihed
        #If its finished it appends to the progress report array.
        for assignment in self.assignment_table :
            if(assignment["course_id"] == course_id and assignment["is_finished"] == "0"):
                   self.progress_report.append(f"{course_name}: {assignment["assignment_name"]}")

     
        await inter.response.send_message(self.progress_report)

def setup(bot):
    bot.add_cog(ProgressCommand(bot))