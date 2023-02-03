import secrets
import os

class Config:
	secret_key=os.environ.get('SECRET_KEY',secrets.token_hex())
	SECRET_KEY=os.environ.get('SECRET_KEY',secrets.token_hex())
	SQLALCHEMY_DATABASE_URI="sqlite:///jflix_data.sqlite"
	SQLALCHEMY_TRACK_MOFICATIONS=True
	SQLALCHEMY_COMMIT_ON_TEARDOWN=True
	MAIL_USERNAME="olatidejoseph17@gmail.com"
	MAIL_USE_TLS=True
	MAIL_PORT=25
	DEBUG=True
	MAIL_SERVER="smtp.gmail.com"
	MAIL_PASSWORD="znlcreowzqdsxoyx"