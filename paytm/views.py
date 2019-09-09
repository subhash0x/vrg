from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils.translation import get_language
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . import Checksum
from paytm.models import PaytmHistory
from blog.models import Post, Order
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.

@login_required
def home(request):
    return HttpResponse("<html><center><a class='btn my-2 my-sm-0' href='"+ settings.HOST_URL +"/paytm/payment'>PayNow</center></html>")


def payment(request):
    game = Post.objects.get(id=request.GET['id'])
    order = Order.objects.create(game=game, owner=request.user)
    MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
    MERCHANT_ID = settings.PAYTM_MERCHANT_ID
    get_lang = "/" + get_language() if get_language() else ''
    CALLBACK_URL = settings.HOST_URL + settings.PAYTM_CALLBACK_URL
    # Generating unique temporary ids
    order_id = Checksum.__id_generator__()

    bill_amount = game.reg_fee
    if bill_amount == 0 :
        order.payment_status = 'TXN_SUCCESS'
        order.save()
        return redirect('/payment?id=' + str(order.game.id) + '&success=true')
    elif bill_amount:
        data_dict = {
                    'MID':MERCHANT_ID,
                    'ORDER_ID':order.id,
                    'TXN_AMOUNT': bill_amount,
                    'CUST_ID': request.user.username,
                    'INDUSTRY_TYPE_ID':'Retail',
                    'WEBSITE': 'DEFAULT',
                    'CHANNEL_ID':'WEB',
                    'CALLBACK_URL':CALLBACK_URL,
                }
        param_dict = data_dict
        #print(param_dict)
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)
        return render(request,"payment.html",{'paytmdict':param_dict})
    return HttpResponse("Bill Amount Could not find. ?bill_amount=10")





@csrf_exempt
def response(request):
    if request.method == "POST":
        MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]
        verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
        if verify:
            order = Order.objects.get(id=data_dict['ORDERID'])
            ph = PaytmHistory.objects.create(user=order.owner, **data_dict)
            order.payment_status = data_dict['STATUS']
            order.save()
            #print(order.payment_status)
            if order.payment_status == 'TXN_SUCCESS':
                return redirect('/payment?id=' + str(order.game.id) + '&success=true')
            else:
                return redirect('/payment?id=' + str(order.game.id) + '&success=false')
        else:
            return HttpResponse("checksum verify failed")
    return HttpResponse(status=200)
