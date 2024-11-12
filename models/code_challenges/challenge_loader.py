import json
import os

from models.code_challenges.challenge import Challenge, DIFFICULTY
from models.code_challenges.challenge_category import ChallengeCategory


class ChallengeLoader:
    """
    Class for loading all challenges from the json file, it will create a json file if it doesn't exist,

    Attributes:
        challenge_file (str): The path to the json file
        challenges (list[ChallengeCategory]): A list of challenge categories, from the json file
    """

    def __init__(self):
        """
        Initialzes the ChallengeLoader with a challenge file path and an empty list of challenges,
        and calls the create_challenge_file method to create the json file if it doesn't exist
        """
        self.challenge_file = 'data/challenges.json'
        self.challenges: list[ChallengeCategory] = []

        self.create_challenge_file()

    def create_challenge_file(self):
        """
        Create a json file with default data if it doesn't exist
        """
        if not os.path.exists('data'):
            os.makedirs('data')

        if not os.path.exists(self.challenge_file):
            with open(self.challenge_file, 'w') as file:
                data = {
                    "challenges": [
                        ChallengeCategory("COMP 333", "Object Oriented C++", [
                            Challenge("Challenge Question", "Challenge Description", DIFFICULTY.EASY),
                        ]).to_dict()
                    ]
                }

                json.dump(data, file, indent=4)

    def get_category(self, category_name: str) -> ChallengeCategory | None:
        """
        Get a challenge category by name

        :param category_name: The name of the category
        :return: The challenge category if found, None otherwise
        """
        for challenge in self.challenges:
            if category_name.lower() in challenge.category.lower():
                return challenge
        return None

    def load(self):
        """
        Load all challenges from the json file, will enforce the structure of the json file
        """
        self.create_challenge_file()

        with open(self.challenge_file, 'r') as file:
            data = json.load(file)

            challenges = data['challenges']

            for challenge in challenges:
                category = challenge['category']
                description = challenge['description']
                challenges = [Challenge(challenge['title'], challenge['description'], challenge['difficulty']) for challenge in challenge['challenge']]

                self.challenges.append(ChallengeCategory(category, description, challenges))
