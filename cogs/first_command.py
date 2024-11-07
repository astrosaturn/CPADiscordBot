import disnake
from disnake.ext import commands

class SlashCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="A simple slash command")
    async def hello(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message("Hello, world!")

def setup(bot):
    bot.add_cog(SlashCommand(bot))