#default
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = 'somthing'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'