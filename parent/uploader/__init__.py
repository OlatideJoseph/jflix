from flask import Blueprint

uploader=Blueprint('uploader',__name__,template_folder='templates',
			static_folder='static',
			static_url_path='/uploader-static')