from flask import Flask, render_template, request, redirect
import os
from todo_app.data import trello_items
from todo_app.flask_config import Config
from todo_app.request_helper import trello

app = Flask(__name__)
app.config.from_object(Config())
BOARD_ID = os.getenv('BOARD_ID')
lists = trello.make_request('GET', f'https://api.trello.com/1/boards/{BOARD_ID}/lists').json()

def name_for_list(id):
    return next((list['name'] for list in lists if list['id'] == id), "Couldn't get status")

@app.route('/')
def index():
    return render_template('index.html', items=trello_items.get_items(BOARD_ID), lists=lists, name_for_list=name_for_list)

@app.route('/add', methods=['POST'])
def add_item():
    trello_items.add_item(request.form['listId'], request.form['title'])
    return redirect('/')

@app.route('/update', methods=['PUT', 'POST'])
def update_item():
    trello_items.save_item(request.form['itemId'], request.form['listId'])
    return redirect('/')
