from dataclasses import field
from django.forms import ModelForm
from .models import Post, Story

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image','user', 'name', 'tag','text']

class StoryModel(ModelForm):
    class Meta:
        model = Story
        fields = '__all__'