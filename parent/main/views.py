from parent.utils import ProfileView
from .forms import UserUpdateForm
class UserProfileView(ProfileView):
	template_name="users/profile.html"
	form=UserUpdateForm