from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils.translation import get_language
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . import Checksum
from paytm.models import PaytmHistory
from blog.models import Post, Student
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.

@login_required
def home(request):
    return HttpResponse("<html><center><a class='btn my-2 my-sm-0' href='"+ settings.HOST_URL +"/paytm/payment'>PayNow</center></html>")


def payment(request):
    student = Student.objects.get(pk=request.GET['id'])
    print(id)
    MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
    MERCHANT_ID = settings.PAYTM_MERCHANT_ID
    get_lang = "/" + get_language() if get_language() else ''
    CALLBACK_URL = settings.HOST_URL + settings.PAYTM_CALLBACK_URL
    print(CALLBACK_URL)
    # Generating unique temporary ids
    order_id = Checksum.__id_generator__()

    bill_amount = student.total_fee
    print(bill_amount)
    if bill_amount == 0 :
        student.payment_status = 'TXN_SUCCESS'
        student.save()
        return redirect('/fee' +'?application_id='+ str(student.application_id) + '&success=true')

    elif bill_amount:
        data_dict = {
                    'MID':MERCHANT_ID,
                    'ORDER_ID':str(student.application_id),
                    'TXN_AMOUNT': bill_amount,
                    'CUST_ID': str(request.user.id),
                    'INDUSTRY_TYPE_ID':'Retail',
                    'WEBSITE': 'DEFAULT',
                    'CHANNEL_ID':'WEB',
                    'CALLBACK_URL':CALLBACK_URL,
                }
        print(data_dict)
        data_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)
        return render(request,"payment.html",{'paytmdict':data_dict})
    return HttpResponse("Bill Amount Could not find. ?bill_amount=10")


@csrf_exempt
def response(request):
    if request.method == "POST":
        MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]
        verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
        print(str(data_dict))
        if verify:
            order = Student.objects.get(pk=data_dict['ORDERID'])
            ph = PaytmHistory.objects.create(user=order, **data_dict)
            order.payment_status = data_dict['STATUS']
            order.save()
            #print(order.payment_status)
            if order.payment_status == 'TXN_SUCCESS':
                return redirect('/fee' +'?application_id=' + str(order.application_id) + '&success=true')
            else:
                return redirect('/fee' +'?application_id=' + str(order.application_id) + '&success=false')
        else:
            return HttpResponse("checksum verify failed")
    return HttpResponse(status=200)
