from django.shortcuts import render, redirect
from django.contrib.auth.models import User


from django.contrib.auth import authenticate, login, logout

def account_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'accounts/login.html', {'error':'Email or Password is Incorrect'})
    return render(request, 'accounts/login.html')

def account_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        user = User(username=username, email=email)
        user.set_password(request.POST.get('password'))
        user.save()
        return redirect('login')
    return render(request, 'accounts/signup.html')