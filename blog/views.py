from django.shortcuts import render
from .models import Post


def ShowBlog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

