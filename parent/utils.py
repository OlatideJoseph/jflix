import functools
from flask import redirect,url_for,flash,render_template,request
from flask.views import View
from flask_login import current_user,login_required
from werkzeug.utils import secure_filename
from PIL import Image
from .main.models import User,db
import secrets
import os

def url_normal_checks(func_view):
	@functools.wraps(func_view)
	def wrap(*args,**kwargs):
	    if current_user.is_verified:
	    	if not current_user.is_suspended:
	    		pass
	    else:
	    	return redirect(url_for('not_verified'))
	    return func_view(*args,**kwargs)
	return wrap

def log_out_required(func):
	'''A wrapper function that that act as the opposite of the flask login required'''
	@functools.wraps(func)
	def wrap_logout(*args,**kwargs):
		if current_user.is_authenticated:
			flash("You need to logout before you can access that page !","warning")
			return redirect(url_for('main.index'))
		return func(*args,**kwargs)

	return wrap_logout
def random_generator():
	import random
	integers=(str(random.randint(1,9)) for i in range(7) )
	randoms=''.join(integers)
	print(randoms)
	return randoms
def username_generator(f_n,l_n,m_n=''):
	username=f_n.title()+m_n.title()+l_n
	try:
		new=random_generator()+'_'+username
		usr=User.query.filter_by(username=new).first()
		if usr:
			new=username_generator(f_n,l_n,m_n)
		return new
	except RecursionError:
		new=username_generator(f_n,l_n,m_n)
		return new


class Config:
	secret_key=os.environ.get('SECRET_KEY')
	SECRET_KEY=os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI="sqlite:///jflix_data.sqlite"
	SQLALCHEMY_TRACK_MOFICATIONS=True
	SQLALCHEMY_COMMIT_ON_TEARDOWN=True
	MAIL_USERNAME=os.environ.get('USER_EMAIL')
	MAIL_USE_TLS=True
	#MAIL_USE_SSL=True
	MAIL_PORT=25
	DEBUG=True
	MAIL_SERVER="smtp.gmail.com"
	MAIL_PASSWORD=os.environ.get('USER_PASSWORD')



class ProfileView(View):
	"""
		A profile view class that inherits from flask view class
		that implements the logic of a view class and make more
		easier in and shorter
	"""
	decorators=[login_required]
	methods=['GET','POST']
	form=''
	template_name="profile/user.html"

	def dispatch_request(self):
		template=self.template_name
		form=self.form()
		if request.method == 'GET': # A get logic for clients data
			form.first_name.data=current_user.first_name
			form.user_name.data=current_user.username
			form.last_name.data=current_user.last_name
			form.middle_name.data=current_user.middle_name
			form.profile_image.data=request.root_path+current_user.img_url
			form.d_o_b.data=current_user.dob
		if form.validate_on_submit(): #checks if the submitted form is valid.
			first_name=form.first_name.data
			last_name=form.first_name.data
			middle_name=form.middle_name.data
			user_name=form.user_name.data
			dob=form.d_o_b.data
			file=form.profile_image.data
			if first_name:
				current_user.first_name=first_name
			if last_name:
				current_user.last_name=last_name
			if middle_name:
				current_user.middle_name=middle_name
			if dob:
				current_user.dob=dob
			if user_name:
				current_user.username=user_name
			if file:	
				filename=file.filename
				filename=secure_filename(filename)
				if filename is not None:
					#changing file extension to webp
					name,_=filename.split('.')
					filename=name+'.webp'
					image_name=current_user.image_name
					current_user.img_url=url_for('static',filename='/users/images/'+filename)
					# checks if the former image exists in the images directory and deletes it
					if image_name:
						path_img=request.root_path+f'/parent/static/users/images/{image_name}'
						print(path_img)
						exists=os.path.exists(path_img)
						if exists:
							os.remove(path_img)
							print("Removed former image")
					current_user.image_name=filename
					img=Image.open(file)
					img.thumbnail((250,250))
					construct=os.path.join(request.root_path,'parent/static/users/images',filename)
					img.save(construct,format="webp")
			db.session.commit()
		return render_template(template,form=form)


class ProfileUpdateView(View):
	decorators=[login_required]
	methods=['GET','POST']
	template="profile/user_update.html"

	def dispatch_request(self):
		pass