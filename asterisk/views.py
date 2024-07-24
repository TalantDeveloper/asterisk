from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        return redirect('main:index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, f"{username} siz tizimga muvafaqqiyatli kirdingiz :)")
                return redirect('main:index')
    return render(request, 'auth/login.html')


def logout_view(request):
    logout(request)
    return redirect('main:index')
