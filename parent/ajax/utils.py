import functools
from flask import request,redirect,url_for,abort,jsonify
from parent.main.models import User
def auth_login_required(func_view):
	@functools.wraps(func_view)
	def wrap(*args,**kwargs):
		auth=request.authorization
	    if not auth:
	    	abort(401,{'message':'login_required','WWW-Authenticate':"Bearer Realm='Login Required !"})
	    username_or_token=auth['username']
	    user=User.query.filter_by(username=username_or_token)
	    if not user:
	    	pass
	    return func_view(*args,**kwargs)
	return wrap