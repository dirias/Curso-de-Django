# Django
from django.contrib import admin
from django.db import models
# Models
from posts.models import Post
# Register the post models on the admin interafce.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin"""
    list_display = ('pk','user', 'title', 'photo', 'created', 'modified')
    list_editable = ('title', 'photo')
    search_fields = ('user', 'title')
    list_filter = ('created', 'modified')

    fieldsets = (
        ('User', {'fields': (('user', 'profile'),)}),
        ('Post', {'fields': (('title', 'photo'),)}),
        ('Metadata', {'fields': (('created', 'modified'),)})
    )

    readonly_fields = ('created', 'modified')