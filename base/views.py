from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .models import *
from .forms import *


def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Пользователь не может войти, скорее всего вас нет в списке зареговшихся, зарегайтесь.')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('base:home')
        else:
            messages.error(request, 'Логин или пароль неправильный')

    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('base:home')

def registersUser(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('base:home')
        else:
            messages.error(request, 'Ошибка при регистрации аккаунта...')

    context = {'form':form}
    return render(request, 'base/login_register.html', context)


def home(request):
    posts = Post.objects.all()
    stories = Story.objects.all()

    context = {'posts': posts, 'stories': stories}
    return render(request, 'base/home.html', context)

def posts(request):
    tags = Tag.objects.all()
    q = request.GET.get('q') if request.GET.get('q') !=None else ''
    # posts = Post.objects.filter(tag__name__icontains = q)
    posts = Post.objects.filter(
        Q(tag__name__icontains=q) |
        Q(name__icontains=q) |
        Q(text__icontains=q)
    )

    posts__cout = posts.count()
    context = {'posts': posts, 'tags': tags, 'posts__cout': posts__cout}
    return render(request, 'base/posts.html', context)

def post(request,pk):
    post = Post.objects.get(id=pk)
    comments = post.comment_set.all().order_by('-created')
    if request.method == 'POST':
        comment = Comment.objects.create(
            user = request.user,
            post = post,
            body = request.POST.get('body')
        )
        return redirect('base:post', pk=post.id)

    context = {'post': post, 'comments': comments}
    return render(request, 'base/post.html', context)

# ! post
@login_required(login_url='base:login')
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('base:posts')

    context = {'form':form}
    return render(request, 'base/create-post.html', context)

@login_required(login_url='base:login')
def updatePost(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.user != post.user:
        return HttpResponse('None')

    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('base:home')

    context = {'form':form}
    return render(request, 'base/create-post.html', context)

@login_required(login_url='base:login')
def deletePost(request,pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('base:home')

    context = {'post':post}
    return render(request, 'base/deletePost.html', context)
    
#! story
@login_required(login_url='base:login')
def createStory(request):
    form = StoryModel()
    if request.method == 'POST':
        form = StoryModel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('base:home')

    context = {'form':form}
    return render(request, 'base/createStory.html', context)

@login_required(login_url='base:login')
def deleteStory(request,pk):
    post = Story.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('base:home')

    context = {'post':post}
    return render(request, 'base/deletePost.html', context)

@login_required(login_url='base:login')
def updateStory(request,pk):
    post = Story.objects.get(id=pk)
    form = StoryModel(instance=post)

    if request.method == 'POST':
        form = StoryModel(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('base:home')

    context = {'form':form}
    return render(request, 'base/createStory.html', context)


class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        if is_dislike:
            post.dislikes.remove(request.user)
        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        if not is_like:
            post.likes.add(request.user)
        if is_like:
            post.likes.remove(request.user)
        return HttpResponseRedirect(reverse('base:post', args=[str(pk)]))

class AddDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        if is_like:
            post.likes.remove(request.user)
        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        if not is_dislike:
            post.dislikes.add(request.user)
        if is_dislike:
            post.dislikes.remove(request.user)
        return HttpResponseRedirect(reverse('base:post', args=[str(pk)]))