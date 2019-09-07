from django.shortcuts import render
from django.urls import path, include
from .models import Post,Student
import datetime
from django.utils import timezone
from django.shortcuts import render_to_response
from django.template import RequestContext


def post_list(request):
    context = {
        'x1' : Post.objects.filter(update_type='News'),
        'x2' : Post.objects.filter(update_type='Tender'),
        'x3' : Post.objects.filter(update_type='Events'),
        'x4' : Post.objects.filter(update_type='other')
        }
    return render(request, 'blog/index.html',context)


def bform(request):
    if request.method == 'POST':
        sname = request.POST.get("name")
        dob = request.POST.get("dob")
        gender = request.POST.get("male")
        # gender = request.POST.get("female")
        # gender = request.POST.get("other")
        fname = request.POST.get("fname")
        mname = request.POST.get("mname")
        rollno = request.POST.get("rnumber")
        sem = request.POST.get("sem")
        address = request.POST.get("address")
        college_name = request.POST.get("college")
        branch = request.POST.get("branch")
        year = request.POST.get("session")
        stype = request.POST.get("stype")
        bform=Student(name=sname,gender=gender,dob=dob,fname=fname,mname=mname,rollno=rollno,sem=sem,address=address,college_name=college_name,branch=branch,year=year,stype=stype)
        bform.save()
    return render(request, 'blog/bform.html', {'title': 'back Form'})



def base(request):
    context = {
        'x1' : Post.objects.filter(update_type='News'),
        'x2' : Post.objects.filter(update_type='Tender'),
        'x3' : Post.objects.filter(update_type='Events')
        }
    return render(request, 'blog/base.html', context)
