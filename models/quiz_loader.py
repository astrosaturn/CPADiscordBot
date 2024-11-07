import json
import os

from models.quiz_category import QuizCategory
from models.quiz_questions import QuizQuestion


class QuizLoader:
    """
    Class for loading all quizzes from the json file, it will create a json file if it doesn't exist, and parse the json file to get all quizzes.

    Attributes:
        quiz_file (str): The path to the json file
        quizzes (list[QuizCategory]): A list of quiz categories, from the json file
    """

    def __init__(self):
        """
        Initializes the QuizLoader with a quiz file path and an empty list of quizzes
        """
        self.quiz_file = 'data/quizzes.json'
        self.quizzes: list[QuizCategory] = []

        # create quiz file
        self.create_quiz_file()

    def create_quiz_file(self):
        """
        Create a json file with default data if it doesn't exist
        """
        if not os.path.exists('data'):
            os.makedirs('data')

        # populate json file with default data, only one quiz so as not to fill this file with a ton of text lol
        if not os.path.exists(self.quiz_file):
            with open(self.quiz_file, 'w') as file:
                data = {
                    "quizzes": [
                        QuizCategory("COMP 333", "Object Oriented C++", [
                            QuizQuestion("What is an instance of a class called?",
                                         ["Object", "Class", "Method", "Variable"], "Object",
                                         "An object is an instance of a class in object-oriented programming."),
                        ]).to_dict()
                    ]
                }

                json.dump(data, file, indent=4)

    def get_category(self, category_name: str) -> QuizCategory | None:
        """
        Get a quiz category by name

        :param category_name: The name of the category
        :return: The quiz category if found, None otherwise
        """
        for quiz in self.quizzes:
            # if string is found in category name
            if category_name.lower() in quiz.name.lower():
                return quiz
        return None

    def load(self):
        """
        Load all quizzes from the json file, and deserialize the json data

        """

        # create quiz file if it doesn't exist
        self.create_quiz_file()

        # load json file
        with open(self.quiz_file, 'r') as file:
            data = json.load(file)

            # deserialize json data
            for quiz in data['quizzes']:
                quiz_category = QuizCategory(quiz['name'], quiz['description'], [])
                for quiz_question in quiz['quiz_questions']:
                    quiz_category.quiz_questions.append(
                        QuizQuestion(quiz_question['question'], quiz_question['options'], quiz_question['answer'],
                                     quiz_question['explanation']))
                self.quizzes.append(quiz_category)
