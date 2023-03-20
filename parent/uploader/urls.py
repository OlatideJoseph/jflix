<<<<<<< HEAD
from parent.uploader import uploader
from . import views


=======
from parent.uploader import uploader
from . import views


>>>>>>> 69055f3de1f41ab8d7aa81f732a965e330c0d931
uploader.add_url_rule('/',view_func=views.UploaderView.as_view('home'))