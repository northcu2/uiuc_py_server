from flask import Flask, render_template, redirect, \
    url_for, request, session, flash, jsonify
from app import app, db
from models import *
from .forms import LoginForm
from functools import wraps


#Requires the user to log in to access the html doc.
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@app.route('/index')
@login_required
def index():
	events = db.session.query(Event).all()
	return render_template('index.html', events=events)

#@app.route('/login', methods=['GET','POST'])
#def login():
#	form = LoginForm()
#	return render_template('login.html', title='Sign In', form=form)
@app.route('/login', methods=['GET', 'POST'])
def login():

    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin': #temp hardcoded user credintials.
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were logged in.')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('login'))

@app.route("/get_event_info")
def get_event_json():
    events = {}
    for c in session.query(Event).all():
        events[c.id] = {
        'Eventname' : c.Eventname,
        'eventStart': c.eventStart,
        }
    return jsonify(events)

@app.route('/results/')
def results():
    results = Event.query.all()
    return jsonify(data=[c.json_dump() for c in results])
