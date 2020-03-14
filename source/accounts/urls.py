from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import register_view, UserDetailView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login_view'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('register/', register_view, name='register_view'),
    path('profile/<pk>/', UserDetailView.as_view(), name='user_detail'),
]


app_name = 'accounts'