from users.apps import UsersConfig
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from users.views import RegisterView, LoginView, UserUpdateView, get_new_password, VerifyEmailView
from django.urls import path, reverse_lazy

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword', get_new_password, name='get_new_password'),
    path('verify_email//<str:token>/', VerifyEmailView.as_view(), name='verify_email'),

    path('password-reset/',
         PasswordResetView.as_view
         (template_name="users/password_reset_form.html",
          email_template_name="users/password_reset_email.html",
          success_url=reverse_lazy("users:password_reset_done")),
         name='password_reset'),

    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view
         (template_name='users/password_reset_confirm.html',
          success_url=reverse_lazy('users:password_reset_complete')
          ),
         name='password_reset_confirm'),

    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
         name='password_reset_done'),

    path('password-reset/complete',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete')

]
