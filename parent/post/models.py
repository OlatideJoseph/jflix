<<<<<<< HEAD
import json
from datetime import datetime
from parent import db

class Post(db.Model):
	__tablename__='post'
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(150),nullable=False)
	text=db.Column(db.Text,nullable=False,unique=True)
	date_written=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
	editable=db.Column(db.Boolean,nullable=False,default=True)
	category=db.Column(db.PickleType,nullable=True)
	images=db.Column(db.PickleType,nullable=True)
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)


	def to_json(self):
		dicti={
		    'post_id':self.id,
		    'title':self.title,
		    'text':self.text,
		    'date':self.category,
		    'writer':self.writer.username
		}
		return json.dumps(dicti)

	def __str__(self):
		return f"""User<{self.writer.username}>.Post<{self.title[15]}"""
	def __repr__(self):
		return f"""User<{self.writer.username}>.Post<{self.title[15]}"""

=======
import json
from datetime import datetime
from parent import db

class Post(db.Model):
	__tablename__='post'
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(150),nullable=False)
	text=db.Column(db.Text,nullable=False,unique=True)
	date_written=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
	category=db.Column(db.PickleType,nullable=True)
	images=db.Column(db.PickleType,nullable=True)
	user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)


	def to_json(self):
		dicti={
		    'post_id':self.id,
		    'title':self.title,
		    'text':self.text,
		    'date':self.category,
		    'writer':self.writer.username
		}
		return json.dumps(dicti)

>>>>>>> 69055f3de1f41ab8d7aa81f732a965e330c0d931
from parent.main.models import User