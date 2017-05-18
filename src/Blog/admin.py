from django.contrib import admin
from Blog.models import Blog_Post, Post_Admin

# Register your models here.

admin.site.register(Blog_Post,Post_Admin)