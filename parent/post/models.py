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

from parent.main.models import User