<<<<<<< HEAD
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms import (StringField,BooleanField,SubmitField,PasswordField,
					BooleanField,TextAreaField,SelectField,RadioField,DateField)
from wtforms.validators import DataRequired,Length,EqualTo,Email,Regexp,ValidationError
from parent.main.models import User

match=r'[^*&_\-@=+^$",.<>!/\\]+[A-Za-z]+$'
name_match=r'''^[A-Za-z0-9_]+$'''
u_name=r'^[A-Za-z0-9_~`]+$'

class UserUpdateForm(FlaskForm):
	profile_image=FileField("UpdateProfile",
		validators=[
			FileAllowed(
				('jpg','jpeg','png'),
			)
		]
	)
	first_name=StringField("FirstName: ",
		validators=[DataRequired(),
		Length(max=15),
		Regexp(match)
		]
		)
	middle_name=StringField('MiddleName:',
		validators=[DataRequired(),
		Length(max=15),
		Regexp(match)
		]
		)
	last_name=StringField("LastName: ",
		validators=[DataRequired(),
		Length(max=15),
		Regexp(match)
		]
		)
	user_name=StringField('Username:',validators=[Length(max=25),Regexp(name_match)])
	d_o_b=DateField('DateTime:')
	modify=SubmitField('Modify')

class LoginForm(FlaskForm):
	username=StringField("Username :*",validators=[DataRequired(),
		Length(min=3,max=25),Regexp(u_name,message="Your username must be alphanumeric")])
	password=PasswordField(None,validators=[DataRequired(),Length(min=8,max=16)])
	remember=BooleanField("Remember me")
	submit=SubmitField("Sign-In")


class MovieForm(FlaskForm):
	movie_name=StringField("Name",validators=[DataRequired(),Regexp(name_match)])
	description=TextAreaField("Describe Your Movie *",validators=[DataRequired()])
	send=SubmitField("Send")


class SignUpUserForm(FlaskForm):
	name=StringField("First Name",validators=[DataRequired(),Length(min=3,max=25),Regexp(name_match)])
	email=StringField("Email",validators=[DataRequired(),Email(),Length(max=120)])
	username=StringField("Username :",validators=[DataRequired(),Length(min=3,max=16),Regexp(name_match)])
	middle_name=StringField("Middle Name",validators=[DataRequired(),Length(min=3,max=25),Regexp(name_match)])
	last_name=StringField("Last Name *",validators=[DataRequired(),Length(min=3,max=25),Regexp(name_match)])
	password=PasswordField("Password *",validators=[DataRequired()])
	net_password=PasswordField("Re-Type Password",validators=[DataRequired(),EqualTo('password')])
	gender=SelectField('Gender *',choices=[("None","None"),('Male','Male'),('Female','Female')])
	send_data=SubmitField('Send')

	def validate_username(self,username=username):
		user=User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError("Sorry a user with that username already exists")
	def validate_email(self,email=email):
		user=User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError("Email is already associated with another account please use another one !")
=======
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import (StringField,BooleanField,SubmitField,PasswordField,
					BooleanField,TextAreaField,SelectField,RadioField)
from wtforms.validators import DataRequired,Length,EqualTo,Email,Regexp,ValidationError
from parent.main.models import User

class LoginForm(FlaskForm):
	username=StringField("Username :*",validators=[DataRequired(),
		Length(min=3,max=25),Regexp("^[a-z0-9_]+$",message="Your username must be alphanumeric")])
	password=PasswordField(None,validators=[DataRequired(),Length(min=8,max=16)])
	remember=BooleanField("Remember me")
	submit=SubmitField("Sign-In")


class MovieForm(FlaskForm):
	movie_name=StringField("Name",validators=[DataRequired()])
	description=TextAreaField("Describe Your Movie *",validators=[DataRequired()])
	send=SubmitField("Send")


class SignUpUserForm(FlaskForm):
	name=StringField("First Name",validators=[DataRequired(),Length(min=8,max=25)])
	email=StringField("Email",validators=[DataRequired(),Email(),Length(max=120)])
	middle_name=StringField("Middle Name",validators=[DataRequired(),Length(min=8,max=25)])
	last_name=StringField("Last Name *",validators=[DataRequired(),Length(min=8,max=25)])
	password=PasswordField("Password *",validators=[DataRequired()])
	net_password=PasswordField("Re-Type Password",validators=[DataRequired(),EqualTo('password')])
	gender=SelectField('Gender *',choices=[("None","None"),('Male','Male'),('Female','Female')])
	send_data=SubmitField('Send')

	def validate_username(self):
		user=User.query.filter_by(email=self.email.data).first()
		if user:
			raise ValidationError("Sorry a user with that email already exists")
>>>>>>> 69055f3de1f41ab8d7aa81f732a965e330c0d931
