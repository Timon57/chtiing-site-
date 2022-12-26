from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Message
class SignInForm(UserCreationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # last_name= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # password1 = forms.(widget=forms.TextInput(attrs={"class":"form-control"}))
    # password2 = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
        

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        #labels = {'body':''}
    def __init__(self,*args,**kwargs): 
        super().__init__(*args,**kwargs)
        self.fields['body'].label = ''
        self.fields['body'].widget.attrs.update({'rows':'2'})
        