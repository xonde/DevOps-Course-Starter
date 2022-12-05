from flask import Flask, render_template, request, redirect
from todo_app.data import session_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template('index.html', items=session_items.get_items())

@app.route('/add', methods=['POST'])
def add_item():
    session_items.add_item(request.form['title'])
    return redirect('/')
