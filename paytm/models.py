from django.db import models
from django.conf import settings

from django.utils import timezone
from blog.models import Student
# Create your models here.

class PaytmHistory(models.Model):
    user = models.ForeignKey(Student,related_name='rel_payment_paytm',on_delete=models.CASCADE)
    ORDERID = models.CharField('ORDER ID', max_length=30)
    TXNDATE = models.DateTimeField('TXN DATE', default=timezone.now)
    TXNID = models.TextField('TXN ID')
    BANKTXNID = models.CharField('BANK TXN ID', null=True,max_length=50, blank=True)
    BANKNAME = models.CharField('BANK NAME', max_length=50, null=True, blank=True)
    RESPCODE = models.IntegerField('RESP CODE')
    PAYMENTMODE = models.CharField('PAYMENT MODE', max_length=10, null=True, blank=True)
    CURRENCY = models.CharField('CURRENCY', max_length=4, null=True, blank=True)
    GATEWAYNAME = models.CharField("GATEWAY NAME", max_length=30, null=True, blank=True)
    MID = models.CharField(max_length=40)
    RESPMSG = models.TextField('RESP MSG', max_length=250)
    TXNAMOUNT = models.FloatField('TXN AMOUNT')
    STATUS = models.CharField('STATUS', max_length=12)

    class Meta:
        app_label = 'paytm'

    def __unicode__(self):
        return self.STATUS
