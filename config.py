import os
#default
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = 'w\xfc\xbf\xcb~s\x1b\xf8\xe42\xb0\xd6\xc1\x19\xa7\xf1\x06t\x83\xc29\xae[~'

	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	
class DevelopmentConfig(BaseConfig):
	DEBUG = True
	
class ProductionConfig(BaseConfig):
	DEBUG = False
