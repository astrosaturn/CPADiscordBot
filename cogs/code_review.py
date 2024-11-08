import disnake
from disnake import Option, TextInputStyle
from disnake.ext import commands

from models.db.database import Database
from models.db.models.stats import Stats
from models.gpt.gpt_manager import GPTManager


class CodeReview(commands.Cog):
    """
    A cog that contains a slash command for performing code reviews.

    Attributes:
        bot (commands.Bot): The bot instance.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Code review")
    async def code_review(self, inter: disnake.ApplicationCommandInteraction):
        """
        A slash command that takes a code snippet as input in a modal, and returns a code review of the input code.

        :param inter: The interaction object from the slash command.
        """

        if not GPTManager.initialized:
            await inter.response.send_message("GPTManager has not been initialized, please contact an admin.", ephemeral=True)
            return

        await inter.response.send_modal(modal=CodeReviewModal())

class CodeReviewModal(disnake.ui.Modal):
    """
    A modal for taking a code snippet as input for a code review. The reason we are using this is that it allows for multi-line input.
    """

    def __init__(self):
        components = [
            disnake.ui.TextInput(
                label="Enter your code snippet",
                placeholder="Paste your code here",
                custom_id="your_code",
                style=TextInputStyle.paragraph
            )
        ]
        super().__init__(title="Code Review", components=components)

    async def callback(self, interaction: disnake.ModalInteraction):
        """
        A callback that generates a code review for the input code snippet.

        :param interaction: The interaction object from the modal.
        """

        your_code = interaction.text_values["your_code"]

        review = await generate_code_review(your_code)

        session = Database.create_session()
        stats = Stats.get_from_user_id(interaction.user.id, session)
        stats.gptApiCalls += 1
        session.commit()
        session.close()

        await interaction.response.send_message(review)


async def generate_code_review(your_code:str):
    """
    Generate a code review for the input code snippet.

    :param your_code: The code snippet to be reviewed.
    :return: str
    """

    # perform code review logic here
    prompt = f"Review the following code snippet and provide suggestions or improvements, keep the response concise and quickly, this message will be shown on Discord, format it for the platform:\n\n{your_code}"

    review = await GPTManager.create_prompt(prompt)

    return review

def setup(bot):
    """
    Adds the CodeReview cog to the bot.

    :param bot: The bot instance.
    """

    bot.add_cog(CodeReview(bot))