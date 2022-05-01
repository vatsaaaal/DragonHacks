from django.contrib import admin
from .models import Forum, Comment, Channel

admin.site.register(Forum)
admin.site.register(Comment)
admin.site.register(Channel)