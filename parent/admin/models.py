from werkzeug.security import generate_password_hash as gph
from parent import db
from parent.main.models import User

class AdminMixin:
	level=db.Column(db.Integer,nullable=False,default=3)


class Admin(User,AdminMixin):
	def __init__(self,*args,**kwargs):
		super(Admin,self).__init__(**kwargs)
		self.is_admin=True
		db.session.commit()

	def verify_admin(self):
		self.is_verified=True
		db.session.commit()

	@classmethod
	def fromdict(cls,obj):
		if obj:
			admin=cls.query.get(obj.get('id'))
			if admin:
			   return admin
		admin=cls(first_name=obj.get('firstName').title(),
			maiden_name=obj.get('maidenName').title(),
			last_name=obj.get('lastName').title(),
			email=obj.get('email'),username=obj.get('username'),
			password=gph(obj.get('password')))
		db.session.add(admin)
		print(admin.username)
		db.session.commit()
		return admin


	def __repr__(self):
		return f"<Admin {self.username.title()}>"
	def __str__(self):
		return "Admin model database"