from flask import render_template,url_for,redirect,request,flash
from flask_login import current_user,login_user,logout_user
from parent.main import main
from parent.main.forms import LoginForm,SignUpUserForm
from parent.main.models import User,Movie,Comment


@main.route("/")
def index():
	return render_template("main/index.html")

@main.route("/signin",methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for("main.index"))
	form=LoginForm()
	nextu=request.args.get('next',"/")
	if form.validate_on_submit():
		username=form.username.data
		password=form.password.data
		remember=form.remember.data
		uobj=User.query.filter_by(username=username).first()
		if uobj:
			if uobj.check_password():
				login_user(uboj,remember=remember)
			flash('Invalid username or password')
		return dict(resp="data invalid")
	return render_template("main/auth/signin.html",form=form)
@main.route("/sign-up")
def addc():
	if current_user.is_authenticated:
		return redirect(url_for('main.index'))
	form=SignUpUserForm()
	if form.validate_on_submit():
		pass
	return render_template("main/auth/signup.html",form=form)
@main.route("/favicon.ico")
def favicon():
	return redirect(url_for('static',filename='icons8-favicon.png'))
@main.app_errorhandler(404)
def notfound(e):
	return {'message':str(e.get_body),"code":str(e.response)},404