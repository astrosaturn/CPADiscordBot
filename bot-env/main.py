import disnake
import os
from dotenv import load_dotenv

class Gravey(disnake.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        print(f'Message received, {message.author}: {message.content}')

# create .env file if not exists
if not os.path.exists('.env'):
    with open('.env', 'w') as f:
        f.write('DISCORD_TOKEN=token_here')


# retrieve token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = disnake.Intents.all()

client = Gravey(intents=intents)
client.run(TOKEN)