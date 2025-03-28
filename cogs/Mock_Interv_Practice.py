import disnake
from disnake.ext import commands
import openai
import os


class CallOpenAI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Practice for the panel and answer a debugging question??")
    async def panel_practice(self, inter: disnake.ApplicationCommandInteraction):
        
        # Retrieve the API key from the environment variable
        openai.api_key = os.getenv("OPENAI_API_KEY#@")
        # APIKEY MUST BE IN .env IN ORDER TO FUNCTION 

        # Check if the API key is set correctly
        if not openai.api_key:
            raise ValueError("API key is missing. Please set the OPENAI_API_KEY environment variable.")

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # selecting gpt model
            messages=[
                {"role": "system", "content": "you will be asking questions relevent to webdev, lua, js and c++ debugging to test devs on there knowledge."},
                {"role": "system","content": "questions should be in regaurds to the debugging side eg.(how would you go about solving a problem in a fresh code base)"},
                #^^^^^^^^^^^both this line and the one above it can be imagined as a pre prompt that is not seen by the user which helps configure how the model will respond ^^^^^^^^^^^^^^
                {"role": "user", "content": "please ask a short question"}
                #^^user prompt STATIC^^
                #NOTE both system and and user prompts should be opptimized for supperior question generation(https://platform.openai.com/docs/guides/text-generation)
            ]
        )
        print("API CALLED")        
        
        await inter.response.send_message(response['choices'][0]['message']['content'])

def setup(bot):
    bot.add_cog(CallOpenAI(bot))