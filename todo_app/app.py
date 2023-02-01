from flask import Flask, render_template, request, redirect
import os
from todo_app.data import trello_items
from todo_app.flask_config import Config
from todo_app.request_helper import trello
from todo_app.view_models.home_view_model import HomeViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    BOARD_ID = os.environ.get('BOARD_ID')

    @app.route('/')
    def index():
        lists = trello.make_request('GET', f'https://api.trello.com/1/boards/{BOARD_ID}/lists').json()
        home_vm = HomeViewModel(trello_items.get_items(BOARD_ID), lists)
        return render_template('index.html', view_model=home_vm)

    @app.route('/add', methods=['POST'])
    def add_item():
        trello_items.add_item(request.form['listId'], request.form['title'])
        return redirect('/')

    @app.route('/update', methods=['PUT', 'POST'])
    def update_item():
        trello_items.save_item(request.form['itemId'], request.form['listId'])
        return redirect('/')

    return app
