<<<<<<< HEAD
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Email,DataRequired



class AdminLoginForm(FlaskForm):
	email=StringField("Email *",validators=[DataRequired(),Email()])
	password=PasswordField("Password",validators=[DataRequired()])
=======
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Email,DataRequired



class AdminLoginForm(FlaskForm):
	email=StringField("Email *",validators=[DataRequired(),Email()])
	password=PasswordField("Password",validators=[DataRequired()])
>>>>>>> 69055f3de1f41ab8d7aa81f732a965e330c0d931
	send_email_pass=SubmitField("Send Email Authenticator")