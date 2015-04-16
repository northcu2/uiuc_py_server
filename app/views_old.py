from flask import render_template
from app import app, db
from models import *
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	events = db.session.query(Event).all()
	return render_template('index.html', events=events)

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)