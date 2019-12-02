from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import RegistrationForm
from django.contrib.auth.models import User

# Create your views here.


def loginPage(request):
    message = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('indexpage')
            else:
                message = "Your account is currently disabled, please contact admin"
        else:
            message = "Incorrect credentials, please check again"
    elif request.user.is_authenticated:
        return redirect('indexpage')
    return render(request, 'logincontrol/login.html', {'message': message})


def logoutuser(request):
    logout(request)
    return redirect('indexpage')


def signup(request):
    message = ""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['cpassword']:
                try:
                    User.objects.get(username=form.cleaned_data['username'])
                    return render(request, 'logincontrol/signup.html', {'message': "Sorry this username is already taken"})
                except User.DoesNotExist:
                    email = form.cleaned_data['email']
                    username = form.cleaned_data['username']
                    password = form.cleaned_data['password']
                    user = User.objects.create_user(username, password=password, email=email)
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect('indexpage')
            else:
                message = "Passwords didn't match, check again"
                return render(request, 'logincontrol/signup.html', {'message': message})
        else:
            print(form.errors)
    return render(request, 'logincontrol/signup.html', {'message': message})
