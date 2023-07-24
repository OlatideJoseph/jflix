from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,TextAreaField,MultipleFileField,SelectField,SubmitField
from wtforms.validators import DataRequired,ValidationError,Length
class PostForm(FlaskForm):
	title=StringField('Article Title',validators=[DataRequired(),Length(min=1,max=250)])
	content=TextAreaField('Article Content',validators=[DataRequired()])
	editable=SelectField(
		'Do You Want Any Body To Modify This ?',
		validators=[DataRequired()],
		choices=[(True,'Yes'),(False,'No')]
		)
	images=MultipleFileField(
		'You SelectField One OR More Files',
		validators=[FileAllowed(('img','png','jpg'))]
		)
	video_clip=FileField('Video Clip',validators=[FileAllowed(('mp4','mkv'))])
	submit=SubmitField("Digitalize")