from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.account_login, name='login'),
    path('signup/', views.account_signup, name='signup'),
]
