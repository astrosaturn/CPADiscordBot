"""
    Gravey Bot - by Eric Poroznik & Julian Seitz & Tyler Moore 
    A community-driven Discord bot created by students of St. Lawrence College (2023-2026).
"""

import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv

from models.db.database import Database
from management.gpt_manager import GPTManager
from management.status_manager import StatusManager

# retrieve token from .env file
load_dotenv()

Database.create_engine('sqlite:///data/database.sqlite')

# import db models
from models.db.models.reminder import Reminder
from models.db.models.stats import Stats
from models.db.models.tracker import TrackerModel

Database.base.metadata.create_all(Database.engine)

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

StatusManager.initialize("data/statuses.json")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

    # get guild members
    members = 0

    for guild in bot.guilds:
        members += guild.member_count

    # select random status
    selected_status = StatusManager.get_random_status()

    activity = disnake.Activity(type=disnake.ActivityType.custom,name="placeholder",state=f"{selected_status}")
    await bot.change_presence(status=disnake.Status.online, activity=activity)


if __name__ == "__main__":
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

# create .env file if not exists
if not os.path.exists('.env'):
    with open('.env', 'w') as f:
        f.write('DISCORD_TOKEN=token_here\n')
        f.write('GPT_API_KEY=api_key\n')

TOKEN = os.getenv('DISCORD_TOKEN')
GPT_API_KEY = os.getenv('GPT_API_KEY')

if TOKEN == 'token_here':
    raise Exception("DISCORD_TOKEN not found in .env file")

if GPT_API_KEY != 'api_key':
    GPTManager.initialize(GPT_API_KEY)

bot.run(TOKEN)
