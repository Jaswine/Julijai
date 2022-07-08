from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registersUser, name='register'),

    path('<str:pk>/like/', views.AddLike.as_view(), name='like'),
    path('<str:pk>/dislike/', views.AddDislike.as_view(), name='dislike'),

    path('', views.home, name='home' ),
    path('posts/', views.posts, name='posts'),
    path('posts/<str:pk>/', views.post, name='post'),

    path('create-post/', views.createPost, name = 'create-post'),
    path('delete-post/<str:pk>/',views.deletePost, name = 'delete-post'),
    path('update-post/<str:pk>/', views.updatePost, name='update-post'),

    path('create-story/', views.createStory, name='create-story'),
    path('delete-story/<str:pk>/', views.deleteStory, name='delete-story'),
    path('update-story/<str:pk>/', views.updateStory, name='update-story')
]
