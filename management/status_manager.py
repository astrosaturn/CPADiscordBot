import json
import os
from random import randint, choice


class StatusManager:
    statuses: list[str] = []

    @classmethod
    def initialize(cls, filename: str):
        if not os.path.exists(filename):
            # create file if not exists
            with open(filename, 'w') as f:
                # dump default statuses as json
                json_data = {
                    "statuses": [
                        "You need to build a brand - scarfman",
                        "It works on my machine :shrug:",
                        "Don't use multiple return statements!",
                        "methodologies",
                        "It's a feature, not a bug",
                        "Check out /quizzes",
                        "Performing mock interviews... :eyes:",
                    ]
                }

                json.dump(json_data, f, indent=4)

                cls.statuses = json_data["statuses"]

        else:
            with open(filename, 'r') as f:
                json_data = json.load(f)
                cls.statuses = json_data["statuses"]

    @classmethod
    def get_random_status(cls) -> str:
        return choice(cls.statuses)


