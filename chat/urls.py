from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('profile/<str:pk>', views.UserProfile, name='user-profile'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logoutPage,name='logout'),
    path('register',views.registerPage,name='register'),
    path('sendmessage/<str:pk>',views.sendMessage,name='send-message'),
    path('messages',views.userMessage,name="user-messages")

]
