from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_homepage, name='workout_homepage'),
    path('search', views.search, name='search'),
]
