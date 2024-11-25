from django.contrib.auth.decorators import login_required
from django.shortcuts import  render
from django.db import models
from django import forms
from django.contrib.auth import get_user_model

from . import models

class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ['title', 'content']

class DeleteBlogForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    
#class Blog(models.Model):
  #  title = models.charField(max_length=200)
   # content=models.TextField()
  #  class Meta:
    
   #     permissions = [
   #         ('change_blog_title', 'Peut changer le titre d’un billet de blog')
   #     ]
        
User = get_user_model()


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']