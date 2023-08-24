from django.urls import path
from .views import profile_views, login_view, logout_view, register_view

urlpatterns = [
    path('profile/', profile_views, name='profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]