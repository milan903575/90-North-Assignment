from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import CustomUser, Message
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chat')
    else:
        form = AuthenticationForm()
    return render(request, 'chat/login.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat')
    else:
        form = CustomUserCreationForm()
    return render(request, 'chat/signup.html', {'form': form})

@login_required
def chat(request):
    users = CustomUser.objects.exclude(id=request.user.id)
    selected_user = request.GET.get('user')
    messages = Message.objects.filter(
        sender__in=[request.user, selected_user],
        receiver__in=[request.user, selected_user]
    ).order_by('timestamp') if selected_user else []
    return render(request, 'chat/chat.html', {
        'users': users,
        'messages': messages,
        'selected_user': selected_user
    })

@login_required
def send_message(request):
    if request.method == "POST":
        receiver_id = request.POST.get('receiver')
        content = request.POST.get('content')
        Message.objects.create(
            sender=request.user,
            receiver_id=receiver_id,
            content=content
        )
    return redirect('chat')
