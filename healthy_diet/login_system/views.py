from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    print('YES1')
    if request.method == "POST":
        print('YES2')
        username = request.POST["username"]
        password = request.POST["password"]
        print('YES3')
        user = authenticate(request, username=username, password=password)
        print('YES4')
        if user is not None:
            print('YES5')
            login(request, user)
            print('YES6')
            return redirect('home')
        else:
            print('YES7')
            messages.success(request, ("It is not correct, Try again"))
            return redirect('login_system')
    else:
        print('YES8')
        messages.success(request, ("It is not correct, Try again"))
        return render(request, 'authenticate/login_system.html', {})