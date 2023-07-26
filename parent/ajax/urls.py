from flask import make_response,request,abort,jsonify
from parent.main.models import User
from parent.ajax import ajax

@ajax.get("/")
def index():
	auth=request.authorization
	return jsonify(dict(this='this'))

@ajax.post("/user-exist/<string:username>/")
def check_user_exists(username):
	email=request.form.get('email',None)
	if email== 'true':
		usr=User.query.filter_by(email=username).first()
		if usr:
			return jsonify(user=True)
		return jsonify(user=False)
	usr=User.query.filter_by(username=username)
	print(username)
	if not usr.first():
		return jsonify(user=username,message='User Does Not Exist',code='error')
	return jsonify(code='success')

@ajax.post('/check_user_data')
def check_data():
	if request.is_json():
		json=request.get_json()
	return make_response

#@