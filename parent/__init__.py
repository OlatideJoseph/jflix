from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_migrate import Migrate


db=SQLAlchemy()
moment=Moment()
mail=Mail()
login_manager=LoginManager()
login_manager.login_message="You need to login please !"
login_manager.login_message_category="info"
login_manager.login_view="main.login"
migrate=Migrate()

def create_app():
	from parent.utils import Config
	app=Flask(__name__,template_folder='template')
	app.config.from_object(Config)
	db.init_app(app) 
	mail.init_app(app)
	migrate.init_app(app,db)
	moment.init_app(app)
	login_manager.init_app(app)
	from parent.admin import admin
	app.register_blueprint(admin,url_prefix='/admin/section')
	from parent.main.urls import main
	app.register_blueprint(main)
	from parent.post.urls import posts
	app.register_blueprint(posts,url_prefix='/post')
	from parent.main.models import User,Post,Comment
	from parent.admin.models import Admin
	@app.shell_context_processor
	def load_context():
		return {'mail':mail,'User':User,'Post':Post,'Comment':Comment,'Admin':Admin}

	return app