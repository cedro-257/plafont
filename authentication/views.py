from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render

# Create your views here.

# import des fonctions login et authenticate

from . import forms 

def logout_user(request):
    
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'blog/home.html')

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})