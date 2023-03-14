from flask import make_response,request,abort,jsonify
from parent.ajax import ajax

@ajax.get("/")
def index():
	auth=request.authorization
	return jsonify(dict(this='this'))