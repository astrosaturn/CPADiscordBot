import disnake
from disnake.ext import commands, tasks
from datetime import datetime, timedelta

class DailyChallenge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="View todays daily coding challenge for a class!")
    async def daily_challenge(self, interaction: disnake.ApplicationCommandInteraction, course: str, difficulty: int):
        courses = ["COMP 1081, COMP 220, COMP 206, COMP 333"]
        """
         ill do this later because i just cannot think of an implementation right now - eric
        """





def setup(bot):
    bot.add_cog(DailyChallenge(bot))