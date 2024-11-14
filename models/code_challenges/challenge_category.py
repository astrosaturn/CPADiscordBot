from random import choice

from models.code_challenges.challenge import Challenge


class ChallengeCategory:
        """
        A class representing a category of coding challenges, in our case this represents different courses

        Attributes:
            category (str): The category of the challenges
            description (str): The description of the category
            challenge (list[Challenge]): A list of challenges in the category
        """

        def __init__(self, category: str, description: str, challenge: list[Challenge]):
            self.category = category
            self.description = description
            self.challenge = challenge

        def to_dict(self):
            """
            Get the dictionary representation of the challenge category
            :return: The dictionary representation of the challenge category
            """

            return {
                "category": self.category,
                "description": self.description,
                "challenge": [challenge.to_dict() for challenge in self.challenge]
            }

        def get_random_challenge(self):
            """
            Get a random challenge from the category
            :return: A random challenge from the category
            """

            return choice(self.challenge)