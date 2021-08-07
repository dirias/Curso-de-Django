"""Users URLs."""
# Django
from django.urls import path

# Models
from users import views

urlpatterns = [
    
    # Management
    path(route='users/login', view=views.login_view, name='login'),
    path(route='users/logout', view=views.logout_view, name='logout'),
    path(route='users/signup', view=views.UserSignupView.as_view(), name='signup'),
    path(route='users/me/profile', view=views.UpdateProfileView.as_view(), name='update_profile'),

    # Posts, class based view
    path(route='<str:username>/', view=views.UserDetailView.as_view(), name='detail'),
]
