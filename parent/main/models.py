from datetime import datetime
from flask import render_template
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
	__tablename__="user"
	id=db.Column(db.Integer,primary_key=True)
	first_name=db.Column(db.String(50),nullable=False)
	maiden_name=db.Column(db.String(50),nullable=True)
	last_name=db.Column(db.String(50),nullable=False)
	email=db.Column(db.String(150),nullable=False,unique=True)
	username=db.Column(db.String(150),nullable=False,unique=True)
	password=db.Column(db.Text,nullable=False)
	dob=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

	is_verified=db.Column(db.Boolean,default=False)
	posts=db.relationship('Post',backref='writer',lazy=True)
	movie=db.relationship('Movie',backref='producer',lazy=True)
	comments=db.relationship('Comment',backref="users",lazy=True)

	@staticmethod
	def generate_password(p):
		password=gph(p)
		return password

	def check_password(self,p):
		password=cph(p,self.password)


	def send_mail(self,email=None,html=None,title=None):
		if email:
			msg=Message("Test Email Address",sender='jflix.com',recipients=[email])
			msg.html="<h1>Hello There Mail System</h1>"
			mail.send(msg)
		else:
			if html and title:
				msg=Message(title,sender='jflix.com',recipients=[f'{self.email}'])
				msg.html=html
			else:
				msg=Message("Test Email Address",sender='jflix.com',recipients=[f'{self.email}'])
				msg.html="<h1>Hello There Mail System</h1>"
			mail.send(msg)
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
	writer=db.Column(db.String(150),nullable=False)
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
	comments=db.relationship("Comment",backref="movies",lazy=True)

class Comment(db.Model):
    __tablename__="comment"
    id=db.Column(db.Integer,primary_key=True)
    comm=db.Column(db.Text,nullable=False)
    movie_id=db.Column(db.Integer,db.ForeignKey('movie.id'),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

from parent.post.models import Post