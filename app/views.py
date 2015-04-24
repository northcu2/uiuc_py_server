
from flask import render_template
from app import app, db
from models import *


@app.route('/')
@app.route('/index')
def index():
    events = db.session.query(Event).all()
    return render_template('index.html', events=events)
