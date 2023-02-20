from threading import Thread
from datetime import datetime
import datetime as dt
import jwt as Serialize
from flask import render_template,current_app,url_for
from flask_login import UserMixin,AnonymousUserMixin
from flask_mail import Message
from werkzeug.security import generate_password_hash as gph
from werkzeug.security import check_password_hash as cph
from parent import db,login_manager,mail




@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))





class AnnonymousUser(db.Model,AnonymousUserMixin):
	id=db.Column(db.Integer,primary_key=True)
	pass




class User(db.Model,UserMixin):
	""" A User class for the jflix user with admin features """
	__tablename__="user"
	id=db.Column(db.Integer,primary_key=True)
	first_name=db.Column(db.String(50),nullable=False)
	maiden_name=db.Column(db.String(50),nullable=True)
	last_name=db.Column(db.String(50),nullable=False)
	email=db.Column(db.String(150),nullable=False,unique=True)
	username=db.Column(db.String(150),nullable=False,unique=True)
	password=db.Column(db.Text,nullable=False)
	dob=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
	is_admin=db.Column(db.Boolean,default=True,nullable=False)
	is_verified=db.Column(db.Boolean,default=False)
	posts=db.relationship('Post',backref='writer',lazy=True)
	movie=db.relationship('Movie',backref='producer',lazy=True)
	movie_like=db.relationship('MovieLike',backref='liker',lazy=True)
	comments=db.relationship('Comment',backref="users",lazy=True)
	comment_liker=db.relationship('CommentLike',backref='liker',lazy=True)

	@staticmethod
	def generate_password(p):
		password=gph(p)
		return password

	def check_password(self,p):
		password=cph(self.password,p)
		return password


	def send_mail(self,email=None,html=None,title=None,body=None):
		from parent import create_app
		if email:
			msg=Message("Test Email Address",sender='jflix.com',recipients=[email])
			msg.html="<h1>Hello There Mail System</h1>"
			mail.send(msg)
		else:
			if html and title:
				msg=Message(title,sender='jflix.com',recipients=[f'{self.email}'])
				msg.html=html
			elif body and title:
				msg=Message(title,sender='Jflix.com',recipients=[f'{self.email}'])
				msg.body=body

			else:
				msg=Message("Test Email Address",sender='jflix.com',recipients=[f'{self.email}'])
				msg.html="<h1>Hello There Mail System</h1>"
			app=create_app()
			with app.app_context() as ctx:
				ctx.push()
				mail.send(msg)
		return 

	def send_async_email(self,*args,**kwargs):
		func=self.send_mail
		Thread(target=func,args=args,kwargs=kwargs).start()
		return None

	def generate_admin_token(self):
		d=datetime.utcnow()+dt.timedelta(minutes=10)
		serial={'id':self.id,"exp":d}
		s=Serialize.encode(serial,current_app.config['SECRET_KEY'],algorithm="HS256")
		return s
	def send_admin_mail(self):
		token=self.generate_admin_token()
		body=f"""
Dear Site Admin,

I hope this email finds you well. I am writing to bring to your attention a concerning matter regarding the security of your website.

Recently, I noticed several unsuccessful login attempts on your website, which indicates that there may be some suspicious activity happening on your site. It is essential that you take action to ensure the security of your users' accounts and your site as a whole.

If you were the one who attempted to log in, I would like to remind you to please use the link provided:{url_for('admin.authenticate',token=token,_external=True)} we sent you to authenticate your login. This will ensure that you are the only person who has access to your account and that no one else can gain unauthorized access.

On the other hand, if you were not the one who tried to log in, I strongly suggest that you view the login statistics to identify any potential unauthorized access attempts. You can then take the necessary measures to secure your website and your users' accounts.

I understand that maintaining the security of a website can be a challenging task, and I appreciate the time and effort that you invest in it. Please do not hesitate to contact me if you require any further assistance or if you have any questions.

Thank you for your time and attention.

Best regards,
{self.first_name.title()}

		"""
		self.send_async_email(title="Jflix Admin Authentication",body=body)
		return None

	def verify_self(self):
		self.is_verified=True
		db.session.commit()
		msg=Message(f"Activated {self.first_name} @ Jflix.com",sender="jflix.com",
			recipients=[f'{self.email}'])
		msg.html=render_template('mails/verify_user.html')
		mail.send(msg)

	@classmethod
	def fromdict(cls,obj):
		if obj:
			user=cls.query.get(obj.get('id'))
			if user:
			   return user
		user=cls(first_name=obj.get('firstName').title(),
			maiden_name=obj.get('maidenName').title(),
			last_name=obj.get('lastName').title(),
			email=obj.get('email'),username=obj.get('username'),
			password=gph(obj.get('password')))
		db.session.add(user)
		print(user.username)
		db.session.commit()
		return user


class Movie(db.Model):
	__tablename__="movie"
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(150),nullable=False)
	detail=db.Column(db.Text,nullable=False)
	category_type=db.Column(db.PickleType,default=['action&drama','sci-fi'])
	category=db.Column(db.String,default="action",nullable=False)
	writer=db.Column(db.String(150),nullable=False)
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
	movie_like=db.relationship('MovieLike',backref='movie_liked',lazy=True)
	comments=db.relationship("Comment",backref="movies",lazy=True)

class Comment(db.Model):
    __tablename__="comment"
    id=db.Column(db.Integer,primary_key=True)
    comm=db.Column(db.Text,nullable=False)
    movie_id=db.Column(db.Integer,db.ForeignKey('movie.id'),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    comment_like=db.relationship('CommentLike',backref='comment',lazy=True)

class CommentLike(db.Model):
	__tablename__='commentlike'
	id=db.Column(db.Integer,primary_key=True)
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
	comment_id=db.Column(db.Integer,db.ForeignKey('comment.id'),nullable=False)

class MovieLike(db.Model):
	__tablename__='movielike'
	id=db.Column(db.Integer,primary_key=True)
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
	movie_id=db.Column(db.Integer,db.ForeignKey('movie.id'),nullable=False)

from parent.post.models import Post