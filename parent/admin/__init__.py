from flask import Blueprint

admin=Blueprint('admin',__name__,static_url_path='admin-static',static_folder='static',
	template_folder='templates')


from parent.admin.urls import *