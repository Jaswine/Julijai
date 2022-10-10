from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from ..models import *
from ..forms import *


#! simple page (home, posts, post)
def home(request):
    posts = Post.objects.all()[:5]
    stories = Story.objects.all()

    context = {'posts': posts, 'stories': stories}
    return render(request, 'base/home.html', context)

def posts(request):
    tags = Tag.objects.order_by('name')
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
    sorted_posts = []
    posts = Post.objects.all()

    for article in posts: #TODO: sort posts
        if post.id != article.id:
            sorted_posts.append(article)

    if request.method == 'POST': #TODO: add comments
        comment = Comment.objects.create(
            user = request.user,
            profileuser = request.user.profileuser,
            post = post,
            body = request.POST.get('body')
        )
        return redirect('base:post', pk=post.id)

    context = {'post': post, 'comments': comments,'posts':sorted_posts[:4]}
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
    form = PostFormUpdate(instance=post)

    if request.method == 'POST':
        form = PostFormUpdate(request.POST,instance=post)
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


#! like and dislike FOR POST
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

#! delete comment
@login_required(login_url='base:login')
def commentDelete(request,pk):
    comment = Comment.objects.get(id=pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('base:home')

    context = {'post':comment}
    return render(request, 'base/deletePost.html', context)   

#!Topic
@login_required(login_url='base:login')
def createTag(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        tag = Tag.objects.create(
            name = request.POST.get('name')
        )
        # return redirect('base:home')

    context = {'tags':tags}
    return render(request,'base/createTopic.html', context)

@login_required(login_url='base:login')
def deleteTag(request,pk):
    tag = Tag.objects.get(id=pk)

    if request.method == 'POST':
        tag.delete()
        return redirect('base:create-tag')

    context = {'tag':tag}
    return render(request, 'base/deletePost.html', context)