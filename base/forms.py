from dataclasses import field
from django.forms import ModelForm
from .models import Post, Story, ProfileUser
from django.contrib.auth.models import User

class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['email']

class ProfileEditForm(ModelForm):
    class Meta:
        model = ProfileUser
        fields = ['birthday', 'img', 'about']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image','name', 'tag','text']

class PostFormUpdate(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'tag','text']

class StoryModel(ModelForm):
    class Meta:
        model = Story
        fields = ['name','tag','video']