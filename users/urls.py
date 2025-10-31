from django.urls import path
from core.views import home
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('home', home, name='home')
]