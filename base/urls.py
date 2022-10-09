from django.urls import path
from .views import home, registration

app_name = 'base'

urlpatterns = [
    #TODO: authorization(login|logout&register)
    path('login/', registration.loginPage, name='login'),
    path('logout/', registration.logoutUser, name='logout'),
    path('register/', registration.registersUser, name='register'),

    #TODO: home
    path('', home.home, name='home' ),
    path('posts/', home.posts, name='posts'),
    path('posts/<str:pk>/', home.post, name='post'),

    #TODO: tags
    path('create-tag/',home.createTag,name='create-tag'),
    path('delete-tag/<str:pk>/',home.deleteTag, name='delete-tag'),

    #TODO: post
    path('create-post/', home.createPost, name = 'create-post'),
    path('delete-post/<str:pk>/',home.deletePost, name = 'delete-post'),
    path('update-post/<str:pk>/', home.updatePost, name='update-post'),

    #TODO: likes for posts
    path('<str:pk>/like/', home.AddLike.as_view(), name='like'),
    path('<str:pk>/dislike/', home.AddDislike.as_view(), name='dislike'),
    path('comment-delete/<str:pk>/', home.commentDelete, name='comment-delete'),

    #TODO: STORY
    path('create-story/', home.createStory, name='create-story'),
    path('delete-story/<str:pk>/', home.deleteStory, name='delete-story'),
    path('update-story/<str:pk>/', home.updateStory, name='update-story'),

     #TODO: likes for story
    # path('<str:pk>/likeStory/', home.AddLikeStory.as_view(), name='like__story'),
    # path('<str:pk>/likeStory/', home.AddDislikeStory.as_view(), name='dislike__story'),

    #TODO: profile
    path('profile/<str:pk>/', registration.Profile, name='profile'),
    path('change-profile/<str:pk>/', registration.updateProfile, name='change-profile'),
]
