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