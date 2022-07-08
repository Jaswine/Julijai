from email.policy import default
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from base.validators import img__size, story_size

# ! contents and tags for this contents
# TODO: tags for posts and stories
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# TODO: Posts - staties
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='static/images/',  validators=[img__size])
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)
    text = RichTextField()
    
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = []
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

# TODO: comment for Post
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    body = models.CharField(max_length=500)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]

# TODO: Some Story
class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL,null=True)
    video = models.FileField(null=True, blank=True, upload_to='static/images', validators=[story_size])
    
    likes = models.ManyToManyField(User, blank=True, related_name='likesStory')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikesStory')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

# TODO: comment for Story
class StoryComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, null=True)
    body = models.CharField(max_length=500)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]