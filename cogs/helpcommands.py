import disnake

from disnake import Embed
from disnake.ext import commands
from enum import Enum

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
            return embed
        case 2:
            pass
        case 3:
            pass

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    menu_options = commands.option_enum({
        "Assignment Trackers" : 1, 
        "Code" : 2,
        "General" : 3
        })
    
    
    
    @commands.slash_command(description="A simple slash command")
    async def help(self, inter: disnake.ApplicationCommandInteraction, option: menu_options):
        embed = get_embed(option)
        await inter.response.send_message(embed=embed)
        

def setup(bot):
    bot.add_cog(HelpCommand(bot))
