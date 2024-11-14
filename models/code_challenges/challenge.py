
class DIFFICULTY:
    """
    Enum for the difficulty of a challenge

    Attributes:
        EASY (str): Easy difficulty
        MEDIUM (str): Medium difficulty
        HARD (str): Hard difficulty
    """
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"

    @classmethod
    def choices(cls):
        """
        Get the choices for the difficulty

        :return: A list of tuples containing the difficulty and the name of the difficulty
        """
        return [
            (cls.EASY, "Easy"),
            (cls.MEDIUM, "Medium"),
            (cls.HARD, "Hard")
        ]

class Challenge:
    """
    A class representing a coding challenge

    Attributes:
        title (str): The title of the challenge
        description (str): The description of the challenge
        difficulty (str): The difficulty of the challenge
    """

    def __init__(self,title, description, difficulty):
        self.title = title
        self.description = description
        self.difficulty = difficulty

    def __str__(self):
        """
        Get the string representation of the challenge
        :return: The string representation of the challenge
        """
        return f"{self.title} - {self.difficulty} ({self.difficulty})"

    def to_dict(self):
        """
        Get the dictionary representation of the challenge

        :return: The dictionary representation of the challenge
        """
        return {
            "title": self.title,
            "description": self.description,
            "difficulty": self.difficulty
        }