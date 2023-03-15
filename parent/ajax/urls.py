from flask import make_response,request,abort,jsonify
from parent.ajax import ajax

@ajax.get("/")
def index():
	auth=request.authorization
	return jsonify(dict(this='this'))


@ajax.post('/check_user_data')
def check_data():
	if request.is_json():
		json=request.get_json()
	return make_response