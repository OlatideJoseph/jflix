from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Email,DataRequired



class AdminLoginForm(FlaskForm):
	email=StringField("Email *",validators=[DataRequired(),Email()])
	password=PasswordField("Password",validators=[DataRequired()])
	send_email_pass=SubmitField("Send Email Authenticator")