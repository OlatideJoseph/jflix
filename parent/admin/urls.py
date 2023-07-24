import functools
from flask import abort,request,render_template,redirect,url_for
from flask_login import current_user
from parent.admin import admin
from parent.admin.views import FirstPageView,AuthenticateView
from parent.main.models import User
from .forms import AdminLoginForm


def admin_login_required(func):
	@functools.wraps(func)
	def wrapper(*args,**kwargs):
		if current_user.is_authenticated and current_user.is_admin:
			pass
		else:
			return redirect(url_for('admin.admin_login',next=url_for(request.endpoint)))
		return func(*args,**kwargs)
	return wrapper

def admin_protected(func):
	@functools.wraps(func)
	def wrapper(*args,**kwargs):
		if current_user.is_admin is False:
			abort(404)
		return func(*args,*kwargs)
	return wrapper
protected=admin_login_required(FirstPageView.as_view('home'))
admin.add_url_rule('/',view_func=protected)
admin.add_url_rule('/authenticate/<token>',view_func=AuthenticateView.as_view('authenticate'))

@admin.errorhandler(400)
def admin_bad_request(e):
	return "Bad Request",400

@admin.errorhandler(403)
def admin_forbidden(e):
	return "You are forbidden",403

@admin.route("/login",methods=["GET","POST"])
def admin_login():
	if current_user.is_authenticated:
		return redirect(url_for('admin.home'))
	form=AdminLoginForm()
	if form.validate_on_submit():
		email=form.email.data
		password=form.password.data
		admin_u=User.query.filter_by(email=email).first()
		print(admin_u.username,admin_u.is_admin)
		if admin_u and admin_u.is_admin:
			print(admin_u.username)
			admchk=admin_u.check_password(password)
			print(admchk)
			if admchk:
				print(admin_u.send_admin_mail())
				return redirect(url_for('admin.home'))
		abort(403)
		
	return render_template("admin/admin_login.html",form=form)