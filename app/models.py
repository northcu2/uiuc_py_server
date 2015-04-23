from app import db

class User(db.Model):
	id = id = db.Column(db.Integer, primary_key=True)
	userName = db.Column(db.String(64), index=True, unique=True)
	userEvents = db.relationship('Event', backref='author', lazy='dynamic')
	
	def __repr__(self):
		return '<User %r>' % (self.userName)

class Event(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	eventName = db.Column(db.String(128), index=True, unique=False)
	eventStart = db.Column(db.DateTime, index=True, unique=False)
	eventEnd = db.Column(db.DateTime, index=True, unique=False)
	eventRepeats = db.Column(db.Boolean)
	eventLat = db.Column(db.Float, precision=64, index=True, unique=False)
	eventLong = db.Column(db.Float, precision=64, index=True, unique=False)
	locationName = db.Column(db.String(64), index=True, unique=False)
	locationAddress = db.Column(db.String(128), index=True, unique=False)
	eventRating = db.Column(db.Integer, index=True, unique=False)
	creatorID = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	def __repr__(self):
		return '<Event %r>' % (self.eventName)
	