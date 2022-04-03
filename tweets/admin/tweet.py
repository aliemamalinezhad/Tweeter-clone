from django.contrib import admin


class TweetAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_display = ['title', 'content','creator']   
    list_filter = ['title']