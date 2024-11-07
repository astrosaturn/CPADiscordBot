import openai


class GPTManager:
    """
    A static class for managing the GPT model

    Attributes:
        apiKey (str): The openai api key
        client (openai.Client): The openai client
        initialized (bool): A flag to check if the GPTManager has been initialized
    """
    apikey = None
    client = None
    initialized = False

    @classmethod
    def initialize(cls, apiKey: str):
        """
        Initializes the GPTManager with an apiKey

        :param apiKey: The openai api key
        """
        try:
            cls.apiKey = apiKey
            cls.client = openai.AsyncClient(api_key=cls.apiKey)
        except Exception as e:
            print(e)
            return

        cls.initialized = True

    @classmethod
    async def create_prompt(cls, prompt: str) -> str:
        """
        Creates a prompt for the GPT model

        :param prompt: The prompt to be used
        :return: The prompt
        """
        completion = await cls.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        message = completion.choices[0].message.content

        return message


