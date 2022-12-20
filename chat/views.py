from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Profile,Message
from .forms import SignInForm,MessageForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
def home(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request,'chat/home.html',context)

def registerPage(request):
    form = SignInForm
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form':form
    }
    return render(request,'chat/register.html',context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        passsword = request.POST['password']
        user = authenticate(request,username=username,password=passsword)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {
    }
    return render(request,'chat/login.html',context)
    
def logoutPage(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
    return render(request,'chat/logout.html')

def sendMessage(request,pk):
    user = User.objects.get(id=pk)
    messages = Message.objects.all()
    form = MessageForm
    if request.method == "POST":
        form = MessageForm(request.POST)
        msg = form.save(commit=False)
        msg.sender = request.user 
        msg.receiver = user
        msg.save()
        return redirect('send-message', user.id)
    context={
        'form':form,
        'user':user,
        'messages':messages,
    }
    return render(request,'chat/sendMessages.html',context)


        
