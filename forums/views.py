from os import name
from django.shortcuts import render, redirect, get_object_or_404
from .models import Forum, Channel, Comment
from django.contrib.auth.models import User
import datetime


def forums_homepage(request):
    forums = Forum.objects.all()
    return render(request, 'forums/forums_homepage.html', {'forums':forums})

def forum_detail(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)
    channels = Channel.objects.filter(forum=forum)
    return render(request, 'forums/forum_detail.html', {'channels':channels, 'forum':forum})

main_channel_id = None

def channel_detail(request, channel_id):
    channel = get_object_or_404(Channel, pk=channel_id)
    global main_channel_id
    main_channel_id = channel_id
    comments = Comment.objects.filter(channel=channel).order_by('-date_created')
    return render(request, 'forums/channel_detail.html', {'channel':channel, 'comments':comments})

def add_comment(request):
    print("HELLO")
    print("MAIN", main_channel_id)
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    channel = get_object_or_404(Channel, pk=main_channel_id)
    comments = Comment.objects.filter(channel=channel).order_by('-date_created')
    if request.method == "POST":
        if request.POST.get('content'):
            content = request.POST.get('content')
            date_created = datetime.datetime.now()
            comment = Comment(content=content, user=user, channel=channel, date_created=date_created)
            comment.save()
            return render(request, 'forums/channel_detail.html', {'channel':channel, 'comments':comments})
        else:
            return render(request, 'forums/channel_detail.html', {'channel':channel, 'comments':comments, "error":"The comment cannot be empty. Please try again!"})
    return render(request, 'forums/channel_detail.html', {'channel':channel, 'comments':comments})