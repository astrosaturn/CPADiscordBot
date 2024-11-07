import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv

from models.gpt.gpt_manager import GPTManager

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

if __name__ == "__main__":
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

# create .env file if not exists
if not os.path.exists('.env'):
    with open('.env', 'w') as f:
        f.write('DISCORD_TOKEN=token_here')
        f.write('GPT_API_KEY=api_key')


# retrieve token from .env file
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GPT_API_KEY = os.getenv('GPT_API_KEY')

if TOKEN == 'token_here':
    raise Exception("DISCORD_TOKEN not found in .env file")

if GPT_API_KEY != 'api_key':
    GPTManager.initialize(GPT_API_KEY)

bot.run(TOKEN)