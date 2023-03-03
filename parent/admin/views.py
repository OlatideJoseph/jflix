import jwt
from flask import render_template,current_app,abort,redirect,flash,url_for
from flask.views import View,MethodView
from flask_login import current_user,login_user,login_required
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
	decorators=[login_required]
	methods=['GET']

	def dispatch_request(self):
		app=current_app._get_current_object()
		endpoints=app.view_functions.keys()
		endpoints=[tuple(endpoint.split('.')) for endpoint in sorted(endpoints)]# split the endpoint int(blueprint,function)
		dict_={}
		for i in endpoints:
		    for j in endpoints:
		    	if i[0] == j[0]:
			    	try:
		    			dict_[i[0]].append(j[1])
		    		except KeyError:
		    			if len(j) == 2:
			    			tst=i[0]
				    		dict_[tst]=[j[1]]
				    	else:
				    		continue
		for key in dict_:
			dict_[key]=set(dict_[key])
		return render_template('admin.html',admins=admin,dict_url=dict_)
