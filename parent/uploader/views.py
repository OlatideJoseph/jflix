<<<<<<< HEAD
import os
from flask import render_template
from flask.views import View
from flask_login import login_required
from .forms import MovieUploadFields
from werkzeug.utils import secure_filename
from parent.uploader import uploader
from parent.utils import ProfileView,ProfileUpdateView
class UploaderView(View):
	methods=['GET','POST']
	decorators=[login_required]

	def dispatch_request(self):
		form=MovieUploadFields()
		if form.validate_on_submit():
			title=form.title.data
			video=form.video.data
			desc=form.desc.data
			if video:
				filename=secure_filename(video.filename)
				if not filename:
					raise(Exception)
				path=os.path.join(uploader.root_path,filename)
				video.save(path)

		return render_template('uploader/home.html',form=form)


class UserProfileView(ProfileView):
	pass
=======
import os
from flask import render_template
from flask.views import View
from flask_login import login_required
from .forms import MovieUploadFields
from werkzeug.utils import secure_filename
from parent.uploader import uploader
from parent.utils import ProfileView,ProfileUpdateView
class UploaderView(View):
	methods=['GET','POST']
	decorators=[login_required]

	def dispatch_request(self):
		form=MovieUploadFields()
		if form.validate_on_submit():
			title=form.title.data
			video=form.video.data
			desc=form.desc.data
			if video:
				filename=secure_filename(video.filename)
				if not filename:
					raise(Exception)
				path=os.path.join(uploader.root_path,filename)
				video.save(path)

		return render_template('uploader/home.html',form=form)


class UserProfileView(ProfileView):
	pass
>>>>>>> 69055f3de1f41ab8d7aa81f732a965e330c0d931
