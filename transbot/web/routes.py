from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bot.reaction_roles import ReactionRole, Base

main = Blueprint('main', __name__)
engine = create_engine('sqlite:///bot.db')
Session = sessionmaker(bind=engine)

@main.route('/')
def index():
    session = Session()
    reaction_roles = session.query(ReactionRole).all()
    return render_template('reaction_roles.html', reaction_roles=reaction_roles)

@main.route('/api/reaction-roles', methods=['POST'])
def create_reaction_role():
    session = Session()
    data = request.json
    
    reaction_role = ReactionRole(
        guild_id=data['guild_id'],
        channel_id=data['channel_id'],
        message_id=data['message_id'],
        emoji=data['emoji'],
        role_id=data['role_id']
    )
    
    session.add(reaction_role)
    session.commit()
    
    return jsonify({'status': 'success'})
