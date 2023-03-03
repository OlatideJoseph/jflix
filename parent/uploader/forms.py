from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Regexp,Length

class MovieUploadFields(FlaskForm):
	title=StringField('Title *',validators=[DataRequired(),Length(min=1,max=120)])
	video=FileField('Movie File *',validators=[FileAllowed(['.mp4','.mkv']),FileRequired()])
	desc=TextAreaField('Description',validators=[DataRequired(),Length(min=10)])
	submit=SubmitField("Submit")