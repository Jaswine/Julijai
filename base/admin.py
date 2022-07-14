from django.contrib import admin
from .models import * 

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'img']

admin.site.register(ProfileUser, ProfileAdmin)
# admin.site.register(Profile)

@admin.register(Post)
class LectionAdmin(admin.ModelAdmin):
    list_display = ['user', 'name','tag', 'updated']

@admin.register(Story)
class LectionAdmin(admin.ModelAdmin):
    list_display = ['name','tag','updated']

admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(StoryComment)
