from parent.uploader import uploader
from . import views


uploader.add_url_rule('/',view_func=views.UploaderView.as_view('home'))