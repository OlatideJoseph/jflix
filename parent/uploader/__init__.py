<<<<<<< HEAD
from flask import Blueprint

uploader=Blueprint('uploader',__name__,template_folder='templates',
			static_folder='static',
=======
from flask import Blueprint

uploader=Blueprint('uploader',__name__,template_folder='templates',
			static_folder='static',
>>>>>>> 69055f3de1f41ab8d7aa81f732a965e330c0d931
			static_url_path='/uploader-static')