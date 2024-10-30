import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET')
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///bot.db')
