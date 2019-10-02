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
        fname = request.POST.get("fname")
        rollno = request.POST.get("rnumber")
        year = request.POST.get("year")
        sem = request.POST.get("sem")
        college_name = request.POST.get("college")
        branch = request.POST.get("branch")
        session = request.POST.get("session")
        stype = request.POST.get("stype")
        regulartyp= request.POST.get("regulartyp")
        privatetyp= request.POST.get("privatetyp")
        portal_fee=40
        total=0
        late_fee=0
        if stype == 'regular':
            application_fee=215
            total=application_fee+late_fee+portal_fee
        elif stype == 'private':
            application_fee=515
            total=application_fee+late_fee+portal_fee
        student = Student.objects.create(
            name=sname,
            dob=dob,
            fname=fname,
            rollno=rollno,
            year=year,
            sem=sem,
            college_name=college_name,
            branch=branch,
            session=session,
            stype=stype,
            regulartyp=regulartyp,
            privatetyp=privatetyp,
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
        return redirect(reverse('paytm-payment') + '?id=' + str(id))
    return render(request, 'blog/fee.html', {'student': student})






def base(request):
    context = {
        'x1' : Post.objects.filter(update_type='News'),
        'x2' : Post.objects.filter(update_type='Tender'),
        'x3' : Post.objects.filter(update_type='Events')
        }
    return render(request, 'blog/base.html', context)


# def payment(request):
#     return render(request, 'payment.html')

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


def activites(request):
 return render(request, 'blog/activites.html')

def contact(request):
    # if request.method == 'POST':
    #     sname = request.POST.get("name")


 return render(request, 'blog/contact.html')

def telephonedir(request):
 return render(request, 'blog/telephonedir.html')
