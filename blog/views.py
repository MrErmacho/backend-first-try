from django.shortcuts import render
from .models import *

def blog(request):
    posts = Post.objects.all
    comments = Comment.objects.all
    return render(request, 'blog/blog.html', {
        'posts': posts,
        'comments': comments
    })

