import disnake

from disnake import Embed
from disnake.ext import commands
from enum import Enum

# Cameron Jack Help Commands


def get_embed(embed_id):
    match embed_id:
        case 1:
            embed = Embed(
                title="Assignment Tracker Commands",
                description="Information about the assignment tracker commands",
                colour=disnake.Colour.blue()
            )
            embed.add_field(
                name="/addtracker", 
                value='''__Arguments__\n`assign_name` The Assignment's name\n`i_date` The due date (DD-MM-YYYY)\n`i_time` Due time (HH-MM)'''
            )
            embed.add_field(
                name="/deletetracker", 
                value='''__Arguments__\n`tracker_id` The tracker ID \n Deletes the tracker '''
            )
            embed.add_field(
                name="/gettrackerbyid", 
                value='''__Arguments__\n`tracker_id` The tracker ID \n Gets the tracker by the ID '''
            )
            embed.add_field(
                name="/viewalltrackers", 
                value='''Press enter to view all trackers '''
            )
            return embed
        case 2:
            embed = Embed(
                title="Code Review",
                description="This command that takes a code snippet as input in a modal, and returns a code review of the input code.",
                colour=disnake.Colour.blue()
            )
            embed.add_field(
                name="/code_review", 
                value='''Input code that you want reviewed.'''
            )
            return embed
        case 3:
            embed = Embed(
                title="Code Challenge",
                description="This command starts a code challenge by displaying a dropdown menu of available code challenge categories",
                colour=disnake.Colour.blue()
            )
            embed.add_field(
                name="/code_challenge", 
                value='''Press enter, a drop down box will appear, select course and a coding challenge will appear.'''
            )
            return embed
        case 4:
            embed = Embed(
                title="Weekly Recap Inserter",
                description="This command is used to add or update the recap for a given course.",
                colour=disnake.Colour.blue()
            )
            embed.add_field(
                name="/add_recap", 
                value='''__Arguments__\n`recap_msg` The recap message that is either being added or updated\n\n A drop down box will appear with which course you would like to add the message to.'''
            )
            return embed
        case 5:
            embed = Embed(
                title="Weekly Recap List",
                description="This command is used to view the weekly recap lists",
                colour=disnake.Colour.blue()
            )
            embed.add_field(
                name="/weekly_recap_list", 
                value='''Press enter, the list of recaps will be listed.'''
            )
            return embed
        case 6:
            embed = Embed(
                title="Daily Tip",
                description="This command is used to prompt a daily generated tip for programming.",
                colour=disnake.Colour.blue()
            )
            embed.add_field(
                name="/daily_tip", 
                value='''Press enter, daily tip will be prompted.'''
            )
            return embed
        case 7:
            embed = Embed(
                title="Panel Practice",
                description="This command is used to practice for the debugging panel to answer a question.",
                colour=disnake.Colour.blue()
            )
            embed.add_field(
                name="/panel_practice", 
                value='''Press enter, a debugging question will be prompted.'''
            )
            return embed
        case 8:
            embed = Embed(
                title="Quizzes",
                description="This command is used to give the user quizzes on any category selected",
                colour=disnake.Colour.blue()
            )
            embed.add_field(
                name="/quizzes", 
                value='''Press enter, a drop down box will appear, select which category you would like to be quizzed on, complete the quizz.'''
            )
            return embed
        case 9:
            embed = Embed(
                title="Reminder",
                description="This command is used to set a reminder for an assignment",
                colour=disnake.Colour.blue()
            )
            embed.add_field(
                name="/remind", 
                value='''__Arguments__\n`name` The Assignment's name\n`due_date` The due date (DD-MM-YYYY)\n`time` Due time (HH-MM)'''
            )
            return embed
        case 10:
            embed = Embed(
                title="Progress Alert",
                description="This command displays the progress of unfinished work from all courses",
                colour=disnake.Colour.blue()
            )
            embed.add_field(
                name="/progress_alert", 
                value='''Press enter, the list of all unfinished work will be listed.'''
            )
            return embed
        

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    menu_options = commands.option_enum({
        "Assignment Tracker Commands" : 1, 
        "Code Review" : 2,
        "Code Challenge" : 3,
        "Weekly Recap Inserter" : 4,
        "Weekly Recap List" :5,
        "Daily Tip" : 6,
        "Panel Practice" : 7,
        "Quizzes" : 8,
        "Reminder" : 9,
        "Progress Alert" : 10
        })
    
    
    
    @commands.slash_command(description="A simple slash command")
    async def help(self, inter: disnake.ApplicationCommandInteraction, option: menu_options):
        embed = get_embed(option)
        await inter.response.send_message(embed=embed)
        

def setup(bot):
    bot.add_cog(HelpCommand(bot))
