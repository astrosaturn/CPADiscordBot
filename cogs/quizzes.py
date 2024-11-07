import disnake
from disnake.ext import commands
from models.quiz_loader import QuizLoader
from random import randint

from models.quiz_questions import QuizQuestion


class QuizzesCommand(commands.Cog):
    """
    A cog that contains a slash command for starting a quiz, and handling the quiz logic.

    Attributes:
        bot (commands.Bot): The bot instance.
        quiz_loader (QuizLoader): An instance of the QuizLoader class.
    """

    def __init__(self, bot, quiz_loader: QuizLoader):
        self.bot = bot
        self.quiz_loader = quiz_loader

    @commands.slash_command(description="Start a quiz")
    async def quizzes(self, inter: disnake.ApplicationCommandInteraction):
        """
        A slash command that starts a quiz by displaying a dropdown menu of available quiz categories,
        and then selecting a random question from the chosen category, triggering a view with buttons for each option.

        :param inter: The interaction object from the slash command.
        """

        # get all available quiz categories
        categories = [quiz.name for quiz in self.quiz_loader.quizzes]

        # check if there are any categories loaded, stop if not
        if not categories:
            await inter.response.send_message("No quiz categories found.", ephemeral=True)
            return

        # create a dropdown menu for selecting a category
        select = disnake.ui.StringSelect(
            custom_id="class_quiz",
            placeholder="Select a class",
            options=[disnake.SelectOption(label=category) for category in categories]
        )

        await inter.response.send_message("Please select a quiz category:", components=[select])

    @commands.Cog.listener("on_dropdown")
    async def select_callback(self, inter: disnake.MessageInteraction):
        """
        A listener that listens for dropdown menu interactions, and sends a random quiz question from the selected category.

        :param inter: The interaction object from the dropdown menu.
        """

        # if its not apart of the quiz command, ignore
        if inter.component.custom_id != "class_quiz":
            return

        category_name = inter.values[0]
        desired_category = self.quiz_loader.get_category(category_name)

        if desired_category is None:
            await inter.response.send_message("Category not found.", ephemeral=True)
            return

        # get a random quiz question
        random_index = randint(0, len(desired_category.quiz_questions) - 1)
        quiz_question = desired_category.quiz_questions[random_index]

        # prepare the question text
        question_text = f"**{quiz_question.question}**\n\n"
        for i, option in enumerate(quiz_question.options):
            question_text += f"{i + 1}. {option}\n"

        # send the question
        await inter.response.send_message(question_text, view=QuizView(quiz_question))


class QuizView(disnake.ui.View):
    """
    A view that displays a quiz question with buttons for each option.

    Attributes:
        quiz (QuizQuestion): The quiz question object.
        correct_answer_index (int): The index of the correct answer.
    """

    def __init__(self, quiz: QuizQuestion):
        """
        Initializes the QuizView with a quiz question object, and creates a button for each option.

        :param quiz: The quiz question object.
        """

        # call the base class constructor
        super().__init__()

        self.quiz = quiz
        self.correct_answer_index = quiz.options.index(quiz.answer)

        # create a button for each option
        for i, option in enumerate(quiz.options):
            button = disnake.ui.Button(label=str(i + 1), style=disnake.ButtonStyle.primary)
            button.callback = self.create_button_callback(i)
            self.add_item(button)

    def create_button_callback(self, index: int):
        """
        Creates a callback function for a button that checks if the answer is correct.

        :param index: The index of the button.
        :return: A callback function, for checking if the answer is correct, meant to be provided to the button.
        """

        async def callback(inter: disnake.MessageInteraction):
            if index == self.correct_answer_index:
                await inter.response.send_message(
                    f"Correct! The answer was: `{self.quiz.answer}` **\n\n{self.quiz.explanation}**")

                for item in self.children:
                    # highlight the correct answer
                    if item.label == str(self.correct_answer_index + 1):
                        item.style = disnake.ButtonStyle.success

                    # disable all buttons
                    item.disabled = True
                await inter.message.edit(view=self)
            else:
                await inter.response.send_message(
                    f"Incorrect! The answer is not: `{self.quiz.options[index]}` \n\n**You may try again.**",
                    ephemeral=True)

        return callback


def setup(bot):
    """
    A function that sets up the quizzes command cog.

    :param bot: The bot instance.
    """
    quiz_loader = QuizLoader()
    quiz_loader.load()

    quizzes_command = QuizzesCommand(bot, quiz_loader)
    bot.add_cog(quizzes_command)
