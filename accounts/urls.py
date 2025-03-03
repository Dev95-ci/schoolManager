from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, login_view, profil

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profil/', profil, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
