from django.urls import path
from . import views

urlpatterns = [
    path('', views.forums_homepage, name='forums_homepage'),
    path('<int:forum_id>', views.forum_detail, name='forum_detail'),
    path('channel/<int:channel_id>', views.channel_detail, name='channel_detail'),
    path('add_comment', views.add_comment, name='add_comment'),
]
