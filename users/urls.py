from django.urls import path
from users.views import register, CustomLoginView, activate_user
from django.contrib.auth.views import LogoutView, PasswordResetCompleteView
from .views import ProfileView, EditProfileView, ChangePassword, CustomPasswordResetView, CustomPasswordResetConfirmView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('sign-out/', LogoutView.as_view(), name='logout'),
    path('activate/<int:user_id>/<str:token>/', activate_user),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),

    path('change-password/', ChangePassword.as_view(), name='change_password'),
    path('reset-password/', CustomPasswordResetView.as_view(), name='reset_password'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='reset_done.html'), name='reset_password_complete'),
]
