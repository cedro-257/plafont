
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from . import forms, models

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect('home')
    return render(request, 'blog/photo_upload.html', context={'form': form})

@login_required
def blog_and_photo_upload(request):
    blog_form = forms.BlogForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        # handle the POST request here
        context = {
        'blog_form': blog_form,
        'photo_form': photo_form,
        }
    return render(request, 'blog/create_blog_post.html', context=context)