from django.urls import path
from django.contrib.auth.views import LogoutView
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('sign-up/', views.sign_up, name='users-sign-up'),
    path('login/', views.login, name='users-login'),
    path('profile/', views.profile, name='users-profile'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name='users-logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password-reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

]
