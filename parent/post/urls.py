from flask import render_template,url_for,redirect,request
from flask_login import login_required
from parent.utils import ListView
from parent.post.views import PostCreateView
from parent.post.models import Post
from . import posts
posts.add_url_rule('/create/',view_func=PostCreateView.as_view('post_create'))
@posts.route("/")
@login_required
def home():
	posts=Post.query.order_by(Post.date_written.desc())
	paginated_posts=posts.paginate(per_page=1,page=3)
	print(paginated_posts.total)
	print(list(paginated_posts.iter_pages()))
	print(dir(paginated_posts))
	return render_template("posts/home.html",posts=posts)