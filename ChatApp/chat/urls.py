from django.urls import path, include

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('chat/', views.chat, name='chat'),
    path('send_message/', views.send_message, name='send_message'),
]
