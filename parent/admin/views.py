import jwt
from flask import render_template,current_app,abort,redirect,flash,url_for
from flask.views import View,MethodView
from flask_login import current_user,login_user
from parent.admin import admin
from parent.main.models import User

class AuthenticateView(MethodView):
	def get(self,token):
		if current_user.is_authenticated:
			return redirect(url_for("admin.home"))
		print(current_app.config['SECRET_KEY'])
		id=jwt.decode(token,current_app.config['SECRET_KEY'],algorithms=['HS256'])
		user=User.query.get(int(id['id']))
		if user:
			login_user(user=user,remember=True)
			flash("Logged in successfully !","info")
			return redirect(url_for('admin.home'))
		else:flash(" invalid user")


class FirstPageView(View):
	methods=['GET']

	def dispatch_request(self):
		return render_template('admin.html')
