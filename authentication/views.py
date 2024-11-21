from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.views.generic import View 
# Create your views here.

# import des fonctions login et authenticate

from . import forms 

                
def logout_user(request):
    
    logout(request)
    return redirect('login')
class LoginPage(View):
    form_class = forms.LoginForm
    template_name =  'authentication/login.html'
    
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form' : form, 'message' : message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
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
                request, self.template_name, context={'form': form, 'message': message})   


def home(request):
    photos = models.Photo.objects.all()
    return render(request, 'blog/home.html'),

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})