from django.shortcuts import render
from django.urls import path, include
from .models import Post
import datetime
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts':posts})

