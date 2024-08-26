from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
	path('login/', UserLoginView.as_view(), name='login'),
	path('logout/', UserLogoutView.as_view(), name='logout'),
]
