from models.quiz.quiz_questions import QuizQuestion

class QuizCategory:
    """
    Class for holding quiz categories, in our usecase, each category refers to a course in our college

    Attributes:
        name (str): The name of the category
        description (str): A description of the category
        quiz_questions (list[QuizQuestion]): A list of quiz questions

    """

    def __init__(self, name:str,description:str, quiz_questions:list[QuizQuestion]):
        """
        Initializes the QuizCategory with a name, description and a list of quiz questions

        """

        self.name = name
        self.description = description
        self.quiz_questions = quiz_questions

    def to_dict(self):
        """
        Convert the object to a dictionary, useful for dumping json data

        :return: dict
        """

        return {
            "name": self.name,
            "description": self.description,
            "quiz_questions": [quiz_question.to_dict() for quiz_question in self.quiz_questions]
        }