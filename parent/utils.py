import functools
from flask import redirect,url_for,flash
from flask.views import View
from flask_login import current_user,login_required

import secrets
import os

def log_out_required(func):
	'''A wrapper function that that act as the opposite of the flask login required'''
	@functools.wraps(func)
	def wrap_logout(*args,**kwargs):
		if current_user.is_authenticated:
			flash("You need to logout before you can access that page !","warning")
			return redirect(url_for('main.index'))
		return func(*args,**kwargs)

	return wrap_logout

class Config:
	secret_key=os.environ.get('SECRET_KEY')
	SECRET_KEY=os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI="sqlite:///jflix_data.sqlite"
	SQLALCHEMY_TRACK_MOFICATIONS=True
	SQLALCHEMY_COMMIT_ON_TEARDOWN=True
	MAIL_USERNAME=os.environ.get('USER_EMAIL')
	MAIL_USE_TLS=True
	#MAIL_USE_SSL=True
	MAIL_PORT=25
	DEBUG=True
	MAIL_SERVER="smtp.gmail.com"
	MAIL_PASSWORD=os.environ.get('USER_PASSWORD')



class ProfileView(View):
	"""
		A profile view class that inherits from flask view class
		that implements the logic of a view class and make more
		easier in and shorter
	"""
	decorators=[login_required]
	methods=['GET']
	template="profile/user.html"

	def dispatch_request(self):
		template=self.template
		user=current_user._get_current_object()
		return render_template(template,user=user)


class ProfileUpdateView(View):
	decorators=[login_required]
	methods=['GET','POST']
	template="profile/user_update.html"

	def dispatch_request(self):
		pass