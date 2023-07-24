from flask import (render_template,url_for,redirect,request,
				flash,session,make_response,jsonify)
from flask_login import current_user,login_user,logout_user,login_required
from parent.utils import log_out_required,url_normal_checks,cache_view
from parent.main import main
from parent.main.views import UserProfileView
from parent.main.forms import LoginForm,SignUpUserForm
from parent.admin.models import Admin
from parent.main.models import User,Movie,Comment,db

main.add_url_rule(
	'/user/profile',
	view_func=UserProfileView.as_view('profile-user')
	)

@main.route("/favicon.ico")
def favicon():
	return redirect(url_for('static',filename='icons8-favicon.png'))

@main.route("/")
def index():
	return render_template("main/index.html")



@main.route("/home")
@login_required
@url_normal_checks
def home(): #Home Page Route
	movies=Movie.query.all()
	return render_template("main/home.html",movie=movies)

@main.route("/movie/detail/<string:hashid>")
@login_required
@url_normal_checks
def movie_detail(hashid):
	movie=Movie.query.filter_by(hashed_id=hashid).first()
	return render_template("main/movie_detail.html",movie=movie)


@main.route("/movies")
@login_required
@url_normal_checks
def movie():
	return "<h1>Movies Pages</h1>"


@main.route("/signin",methods=['GET','POST'])
def login(): #Application Login Route
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
			if uobj.check_password(password):
				login_user(uobj,remember=remember)
				flash("You've been logged in successfully !",'info')
				return redirect('/') if not nextu else redirect(nextu)
			flash('Invalid username or password',"error")
	return render_template("main/auth/signin.html",form=form)

@main.get("/logged-out")
@log_out_required
def logout():
	username=request.args.get('username')
	flash(f'User {current_user.username} has been logged out !','Warning')
	return render_template('users/logged-out.html',username=username)

@main.route('/sign-out')
def log_out_user():
	username=''
	if current_user.is_authenticated:
		username=current_user.username
	logout_user()
	return redirect(url_for('main.logout')) if not username else \
	    redirect(url_for('main.logout',username=username))

@main.route("/sign-up",methods=['GET','POST'])
def addc():
	if current_user.is_authenticated:
		return redirect(url_for('main.index'))
	form=SignUpUserForm()
	if request.headers.get("content-type","application/html") == "application/json":
		rargs=request.args
		return redirect(url_for('ajax.home'),**rargs)
	if form.errors:
		print('errors',form.errors)
	if form.validate_on_submit():
		is_ajax=request.args.get('isajax') == 'true'
		print('passed')
		fn=form.name.data.strip()
		ln=form.last_name.data.strip()
		em=form.email.data.strip()
		un=form.username.data.strip()
		pd=User.generate_password(form.password.data)
		gd=form.gender.data
		user=User(
			first_name=fn,
			last_name=ln,
			email=em,username=un,gender=gd,
			password=pd

			)
		db.session.add(user)
		db.session.commit()
		return jsonify({'Created':True},201) if is_ajax else redirect(url_for('main.login'))
	return render_template("main/auth/signup.html",form=form)

@main.route("/user/verification")
def user_verification():
	return
@main.route("/user/not/verified")
def not_verified():
	return render_template("main/users/not_verified.html")

@main.app_errorhandler(404)
def notfound(e):
	resp={'message':str(e.get_body),"code":str(e.response)}
	if request.is_json:
		return make_response(resp,404,{'Content-Type':'application/json'})
	return render_template('errors/not_found.html')

@main.app_errorhandler(500)
def internal_server_error(e):
	return jsonify(
		{'message':'An error has occured within the server',
		"code":str(500)},500)
