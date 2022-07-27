from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registersUser, name='register'),

    path('', views.home, name='home' ),
    path('posts/', views.posts, name='posts'),
    path('posts/<str:pk>/', views.post, name='post'),

    path('create-tag/',views.createTag,name='create-tag'),
    path('delete-tag/<str:pk>/',views.deleteTag, name='delete-tag'),

    path('create-post/', views.createPost, name = 'create-post'),
    path('delete-post/<str:pk>/',views.deletePost, name = 'delete-post'),
    path('update-post/<str:pk>/', views.updatePost, name='update-post'),
    path('<str:pk>/like/', views.AddLike.as_view(), name='like'),
    path('<str:pk>/dislike/', views.AddDislike.as_view(), name='dislike'),
    path('comment-delete/<str:pk>/', views.commentDelete, name='comment-delete'),

    path('create-stor-y/', views.createStory, name='create-story'),
    path('delete-story/<str:pk>/', views.deleteStory, name='delete-story'),
    path('update-story/<str:pk>/', views.updateStory, name='update-story'),
    path('<str:pk>/likeStory/', views.AddLikeStory.as_view(), name='like__story'),
    path('<str:pk>/likeStory/', views.AddDislikeStory.as_view(), name='dislike__story'),

    path('profile/<str:pk>/', views.Profile, name='profile'),
    path('change-profile/<str:pk>/', views.updateProfile, name='change-profile'),
]
