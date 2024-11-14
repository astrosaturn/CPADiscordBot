import disnake
from disnake.ext import commands

from models.code_challenges.challenge_loader import ChallengeLoader


class CodeChallenge(commands.Cog):
    """
    A cog that contains a slash command for starting a code challenge, and handling the code challenge logic.

    Attributes:
        bot (commands.Bot): The bot instance.
        challenge_loader (ChallengeLoader): An instance of the ChallengeLoader class.
    """

    def __init__(self, bot, challenge_loader: ChallengeLoader):
        self.bot = bot
        self.challenge_loader = challenge_loader

    @commands.slash_command(description="Start a code challenge")
    async def code_challenge(self, inter):
        """
        A slash command that starts a code challenge by displaying a dropdown menu of available code challenge categories,

        :param inter: The interaction object from the slash command.
        """
        categories = [challenge.category for challenge in self.challenge_loader.challenges]

        if not categories:
            await inter.response.send_message("No code challenge categories found.", ephemeral=True)
            return

        select = disnake.ui.Select(
            custom_id="code_challenge",
            placeholder="Select a course",
            options=[disnake.SelectOption(label=category) for category in categories]
        )

        await inter.response.send_message("Please select a code challenge category:", components=[select],
                                          ephemeral=True)

    @commands.Cog.listener("on_dropdown")
    async def select_callback(self, inter: disnake.MessageInteraction):
        """
        A listener that listens for dropdown menu interactions,
        and sends a random code challenge from the selected category.

        :param inter: The interaction object from the dropdown menu.
        :return:
        """
        if inter.component.custom_id != "code_challenge":
            return

        category = inter.values[0]
        challenge_category = self.challenge_loader.get_category(category)

        if not challenge_category:
            await inter.response.send_message("No code challenge category found.", ephemeral=True)
            return

        challenge = challenge_category.get_random_challenge()
        await inter.response.send_message(
            f"**{challenge.title}** - Difficulty: **{challenge.difficulty}**\n\n{challenge.description}",
            ephemeral=True)


def setup(bot):
    """
    Add the CodeChallenge cog to the bot.
    :param bot: The bot instance.
    """

    challenge_loader = ChallengeLoader()
    challenge_loader.load()

    bot.add_cog(CodeChallenge(bot, challenge_loader))
