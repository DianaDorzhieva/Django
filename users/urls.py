from users.apps import UsersConfig
from django.contrib.auth.views import LogoutView
from users.views import RegisterView, LoginView
from django.urls import path


app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register')
]

