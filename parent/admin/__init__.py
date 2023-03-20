<<<<<<< HEAD
from flask import Blueprint

admin=Blueprint('admin',__name__,static_url_path='admin-static',static_folder='static',
	template_folder='templates')


=======
from flask import Blueprint

admin=Blueprint('admin',__name__,static_url_path='admin-static',static_folder='static',
	template_folder='templates')


>>>>>>> 69055f3de1f41ab8d7aa81f732a965e330c0d931
from parent.admin.urls import *