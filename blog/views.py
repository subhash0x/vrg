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
    return render(request, 'blog/bform.html', {'title': 'back Form'})
        #application_fee=request.POST.get("appfee")
        application_fee=0
        if stype == 'Regular':
            application_fee=300
            portal_fee=40
            late_fee=0
            total_fee=application_fee+late_fee+portal_fee
            print("wow")
            print(application_fee)
        print("not working")
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
            total_fee=total_fee,
            late_fee=late_fee,
            portal_fee=portal_fee
        )

    return render(request, 'blog/fee.html', {'title': 'back Form', 'student': student})



def base(request):
    context = {
        'x1' : Post.objects.filter(update_type='News'),
        'x2' : Post.objects.filter(update_type='Tender'),
        'x3' : Post.objects.filter(update_type='Events')
        }
    return render(request, 'blog/base.html', context)




def payment(request):
    # gameId = request.GET['id']
    # print(gameId)
    # game = Post.objects.get(id=gameId)
    # context = {'game' : game }
    # success = request.GET.get('success', None)
    #
    # if success is not None:
    #     print(success)
    #     if success == 'true':
    #         context['paymentSuccess'] = True
    #     else:
    #         context['paymentFailed'] = True
    # if game.orders.filter(owner=request.user, payment_status='TXN_SUCCESS').exists():
    #     context['user_has_paid'] = True
    return render(request, 'payment.html')
