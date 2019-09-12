from django.shortcuts import render,redirect
from django.urls import path, include ,reverse
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
        gender = request.POST.get("gender")
        fname = request.POST.get("fname")
        mname = request.POST.get("mname")
        rollno = request.POST.get("rnumber")
        sem = request.POST.get("sem")
        address = request.POST.get("address")
        college_name = request.POST.get("college")
        branch = request.POST.get("branch")
        year = request.POST.get("session")
        stype = request.POST.get("stype")

        if stype == 'Regular':
            application_fee=300
            portal_fee=40
            late_fee=0
            total=0
            total=application_fee+late_fee+portal_fee
            print("wow")
            print(application_fee)

        student = Student.objects.create(
            name=sname,
            gender=gender,
            dob=dob,
            fname=fname,
            mname=mname,
            rollno=rollno,
            sem=sem,
            address=address,
            college_name=college_name,
            branch=branch,
            year=year,
            stype=stype,
            application_fee=application_fee,
            total_fee=total,
            late_fee=late_fee,
            portal_fee=portal_fee
            )
        return redirect(reverse('feepayment') + '?application_id=' + str(student.application_id))
        #return redirect('/fee.html',{'title': 'back Form', 'student': student})
    return render(request, 'blog/bform.html')









def fee(request):
    id = request.GET.get('application_id')
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        return render(request, 'payment/')

    return render(request, 'blog/fee.html', {'student': student})



def base(request):
    context = {
        'x1' : Post.objects.filter(update_type='News'),
        'x2' : Post.objects.filter(update_type='Tender'),
        'x3' : Post.objects.filter(update_type='Events')
        }
    return render(request, 'blog/base.html', context)


def payment(request):

    return render(request, 'payment.html')







def gallery(request):
 return render(request, 'blog/gallery.html')

def science(request):
  return render(request, 'blog/science.html')

def homescience(request):
  return render(request, 'blog/homescience.html')

def selffinancecourses(request):
 return render(request, 'blog/selffinancecourses.html')

def arts(request):
  return render(request, 'blog/arts.html' )
