import disnake
import os
from dotenv import load_dotenv

class Gravey(disnake.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        print(f'Message received, {message.author}: {message.content}')

# create .env file if not exists
with open('.env', 'a') as f:
    f.write('DISCORD_TOKEN=token_here')

# retrieve token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = Gravey()
client.run(TOKEN)