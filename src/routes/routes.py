import os

from flask import Blueprint
from controllers.controller_music import list_music, add_music, edit_music, del_music
from controllers.controller_user import add_user, authenticar, logout

TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')

main = Blueprint('main', __name__, template_folder=TEMPLATE_DIR)

main.add_url_rule('/', 'list_music', list_music)
main.add_url_rule('/add_music', 'add_music', add_music, methods=['GET','POST'])
main.add_url_rule('/add_user', 'add_user', add_user, methods=['GET','POST'])
main.add_url_rule('/authenticar', 'authenticar', authenticar, methods=['GET','POST'])
main.add_url_rule('/logout', 'logout', logout)
main.add_url_rule('/edit_music/<int:music_id>', 'edit_music', edit_music, methods=['GET','POST'])
main.add_url_rule('/del_music/<int:music_id>', 'del_music', del_music)