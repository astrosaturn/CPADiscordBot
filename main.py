import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv

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


# retrieve token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)