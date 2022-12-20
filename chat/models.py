from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='images')
    

    def __str__(self):
        return f'{self.user.username} Profile'

class Message(models.Model):
    body = models.TextField()
    #related_name is for reverse relation with User (in place user_set,use related_name)
    sender = models.ForeignKey(User,related_name='sentmessages',on_delete=models.SET_NULL,null=True)
    receiver = models.ForeignKey(User,related_name='receivedmessages',on_delete=models.SET_NULL,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:10]
