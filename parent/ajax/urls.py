from flask import make_response,jsonify,request
from parent.ajax import ajax

@ajax.get("/")
def index():
	print(request)
	return make_response(jsonify(this=1),201,{'cache-control':'no-cache','www-Authenticate':'true'})