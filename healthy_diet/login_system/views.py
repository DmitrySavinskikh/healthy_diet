from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm



def goto_firstpage(request):
    return render(request, 'authenticate/first_page_login.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("It is not correct, Try again"))
            return redirect('login_user')
    else:
        messages.success(request, ("It is not correct, Try again"))
        return render(request, 'authenticate/login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ("Yoy were logged out!"))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'authenticate/register_user.html', {
		'form':form,
		})