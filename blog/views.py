from django.shortcuts import render
from django.urls import path, include
from .models import Post
import datetime
from django.utils import timezone



    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

def post_list(request):
    context = {
        'x1' : Post.objects.filter(update_type='News'),
        'x2' : Post.objects.filter(update_type='Tender'),
        'x3' : Post.objects.filter(update_type='Events')
        }
    return render(request, 'blog/index.html',context)





def base(request):
    context = {
        'x1' : Post.objects.filter(update_type='News'),
        'x2' : Post.objects.filter(update_type='Tender'),
        'x3' : Post.objects.filter(update_type='Events')
        }
    # posts = Post.objects.all()
    return render(request, 'blog/base.html', context)
