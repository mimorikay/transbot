import discord
from discord.ext import commands

class ReactionRoleBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.reactions = True
        intents.message_content = True
        intents.guilds = True
        super().__init__(command_prefix='!', intents=intents)
        
    async def setup_hook(self):
        await self.load_extension('bot.reaction_roles')
        
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

