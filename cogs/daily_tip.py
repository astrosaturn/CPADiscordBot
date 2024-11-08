from random import randint

import disnake
from disnake.ext import commands

from models.db.database import Database
from models.db.models.stats import Stats
from models.gpt.gpt_manager import GPTManager


class DailyTip(commands.Cog):
    """
    A cog that contains a slash command for generating a daily programming tip.

    Attributes:
        bot (commands.Bot): The bot instance.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Get a daily tip programming tip, from one of our courses, using AI.")
    async def daily_tip(self, inter: disnake.ApplicationCommandInteraction):
        """
        A slash command that returns a daily programming tip.

        :param inter: The interaction object from the slash command.
        """

        if not GPTManager.initialized:
            await inter.response.send_message("GPTManager has not been initialized, please contact an admin.", ephemeral=True)
            return

        # TODO: Introduce a more dynamic way to get courses, for now, we will use a hardcoded list
        # I want this to be in a config, but for now, we will hardcode it cuz i'm lazy lol
        current_courses = [
            "Object Oriented C++",
            "Operating Systems Linux, z/OS, TSO/ISPF",
            "PHP Programming",
            "Web Programming with Javascript"
        ]

        # get a random course
        random_index = randint(0, len(current_courses) - 1)
        course = current_courses[random_index]

        await inter.response.send_message("Generating daily tip...")

        tip = await self.get_daily_tip(course)

        session = Database.create_session()
        stats = Stats.get_from_user_id(inter.author.id, session)
        stats.gptApiCalls += 1
        session.commit()
        session.close()

        await inter.edit_original_message(content=tip)

    async def get_daily_tip(self, course:str):
        """
        Prompts ChatGPT to generate a daily tip for a specific course.

        :param course: The course to generate a tip for.
        :return: The generated tip.
        """

        prompt = f"Generate a daily tip for the following subject, this will be sent to a Discord server, format it for Discord, ensure the formatting does not get broken. Keep it concise, under 200 words, just send the tip do not respond this prompt otherwise: {course}"
        tip = await GPTManager.create_prompt(prompt)

        return tip

def setup(bot):
    bot.add_cog(DailyTip(bot))