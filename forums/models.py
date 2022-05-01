from hashlib import blake2b
from django.db import models

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Forum(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='media/')
    desc = models.TextField()
    participants = models.ManyToManyField(User)
  
    def __str__(self):
       return self.name


class Channel(models.Model):
    name = models.CharField(max_length=100)
    forum = models.ForeignKey("Forum", on_delete=models.CASCADE)
    desc = models.TextField()
    participants = models.ManyToManyField(User)
  
    def __str__(self):
       return self.name


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    channel = models.ForeignKey("Channel", on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField()
  
    def __str__(self):
       return str(self.user)+": "+str(self.content)[0:15]
