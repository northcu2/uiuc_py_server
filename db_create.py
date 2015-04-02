#This file may no longer be needed.
from app import db
from models import BlogPost

db.create_all()

db.session.add(BlogPost("Good","This SQLALC post is good"))
db.session.add(BlogPost("better","This SQLALC post is better"))


db.session.commit()