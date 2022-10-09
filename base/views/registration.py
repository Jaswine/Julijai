from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages

from ..models import *
from ..forms import *

# ! regestration, login and logout
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
            new_user = form.save(commit=False)
            new_user.save()
            profile = ProfileUser.objects.create(user=new_user)
            login(request, new_user)
            return redirect('base:change-profile', pk=new_user.id)
            # return redirect('base:home')
        else:
            messages.error(request, 'Ошибка при регистрации аккаунта...')

    context = {'form':form}
    return render(request, 'base/login_register.html', context)

#! profile
def Profile(request,pk):
    user = User.objects.get(id=pk)
    profileUser = ProfileUser.objects.get(id=pk)
    posts = Post.objects.all()[:3]
    comments = user.comment_set.all()

    context = {'user':user, 'posts': posts,'comments': comments, 'profileUser': profileUser}
    return render(request, 'base/profile.html', context)

@login_required(login_url='base:login')
def updateProfile(request,pk):
    user = User.objects.get(id=pk)
    UserForm = UserEditForm(instance=user)
    ProfileForm = ProfileEditForm(instance=user.profileuser)

    if request.method == 'POST':
        UserForm = UserEditForm(request.POST, instance=user)
        ProfileForm = ProfileEditForm(request.POST, request.FILES, instance=user.profileuser)
        if ProfileForm.is_valid():
            UserForm.save()
            ProfileForm.save()
            return redirect('base:home')

    context = {'user': user,'UserForm': UserForm,'ProfileForm': ProfileForm}
    return render(request, 'base/profileForm.html', context)