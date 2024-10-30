import discord
from discord.ext import commands
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class ReactionRole(Base):
    __tablename__ = 'reaction_roles'
    
    id = Column(Integer, primary_key=True)
    guild_id = Column(Integer)
    channel_id = Column(Integer)
    message_id = Column(Integer)
    emoji = Column(String)
    role_id = Column(Integer)

class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.engine = create_engine('sqlite:///bot.db')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.user_id == self.bot.user.id:
            return

        reaction_role = self.session.query(ReactionRole).filter_by(
            message_id=payload.message_id,
            emoji=str(payload.emoji)
        ).first()

        if reaction_role:
            guild = self.bot.get_guild(payload.guild_id)
            role = guild.get_role(reaction_role.role_id)
            member = guild.get_member(payload.user_id)
            
            if role and member:
                await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.user_id == self.bot.user.id:
            return

        reaction_role = self.session.query(ReactionRole).filter_by(
            message_id=payload.message_id,
            emoji=str(payload.emoji)
        ).first()

        if reaction_role:
            guild = self.bot.get_guild(payload.guild_id)
            role = guild.get_role(reaction_role.role_id)
            member = guild.get_member(payload.user_id)
            
            if role and member:
                await member.remove_roles(role)

async def setup(bot):
    await bot.add_cog(ReactionRoles(bot))

# web/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    
    from web.routes import main
    app.register_blueprint(main)
    
    return app
