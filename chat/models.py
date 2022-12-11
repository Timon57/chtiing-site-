from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='images')
    

    def __str__(self):
        return f'{self.user.username} Profile'

class Message(models.Model):
    body = models.TextField()
    owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:10]
