import asyncio
from bot.client import ReactionRoleBot
from web import create_app
from config import DISCORD_TOKEN
import threading

def run_flask():
    app = create_app()
    app.run(host='0.0.0.0', port=8080)

def main():
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    
    # Start Discord bot
    bot = ReactionRoleBot()
    bot.run(DISCORD_TOKEN)

if __name__ == '__main__':
    main()
