import os
from flask import request,render_template,current_app,flash,redirect,url_for
from flask_login import current_user,login_required
from werkzeug.utils import secure_filename
from parent.utils import BaseModelView
from parent.post.models import Post
from parent.post.forms import PostForm
from parent import db
from PIL import Image
class PostCreateView(BaseModelView):
	model=Post
	methods=['POST','GET']
	decorators=[login_required]
	template_name='posts/post_create.html'
	init_every_request=True
	def dispatch_request(self,template=template_name):
		r={'writer':current_user}
		template=template
		form=PostForm()
		model=self.model
		print(form.validate_on_submit())
		if form.validate_on_submit():
			print("proceeded")
			title = form.title.data.strip().title()
			content= form.content.data.strip()
			editable=form.editable.data
			r['title']=title
			r['text']=content
			r['editable']=bool(editable) if editable else editable
			if form.images.data:
				path=os.path.join(current_app._get_current_object().root_path,'static/images/posts')
				images=form.images.data
				r['images']=[]
				for image in images:
					if image.filename:#check if there is an actual file uploaded
						print(image.filename)
						name=secure_filename(image.filename)
						pillow=Image.open(image)
						if pillow.size[0] > 640 or pillow.size[1] >480  :
							pillow.thumbnail((640,480))
						if name is not None:
							r['images'].append(secure_filename(name))
							pillow.save(path+name)
							flash("File Uploaded Successfully",'info')
			if form.video_clip.data:
				video_clip=form.video_clip.data
				r['clip']=secure_filename(video_clip.filename)
				video_clip.save(r['clip'])
			post=self.__class__.model(**r)
			db.session.add(post)
			db.session.commit()
			return redirect(url_for('posts.home'))
		return render_template(template,form=form)