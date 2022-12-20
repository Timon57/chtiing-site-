from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Message
class SignInForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        labels = {'body':''}
