
class QuizQuestion:
    """
    Class for holding quiz questions

    Attributes:
        question (str): The question to be asked
        options (list[str]): A list of options to choose from
        answer (str): The correct answer
        explanation (str): An explanation of the answer
    """

    def __init__(self, question:str, options:list[str], answer:str, explanation:str):
        """
        Initializes the QuizQuestion with a question, set of options, answer (matching an option)
        and explanation as to why the answer is correct

        """

        self.question = question
        self.options = options
        self.answer = answer
        self.explanation = explanation

    def to_dict(self):
        """
        Convert the object to a dictionary, useful for dumping json data

        :return: dict
        """

        return {
            "question": self.question,
            "options": self.options,
            "answer": self.answer,
            "explanation": self.explanation
        }