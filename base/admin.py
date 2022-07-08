from django.contrib import admin
from .models import * 

@admin.register(Post)
class LectionAdmin(admin.ModelAdmin):
    list_display = ['user', 'name','tag', 'updated']

@admin.register(Story)
class LectionAdmin(admin.ModelAdmin):
    list_display = ['name','tag','updated']

admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(StoryComment)
