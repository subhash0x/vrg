from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime

category= (
    ('News','Student Notice Board'),
    ('Events','Events / Workshops / Conferences'),
    ('other','Staff Notice Board'),
)

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    update_type = models.CharField(max_length=20, choices=category, default='News')
    specifications = models.FileField(upload_to='router_specifications',default='null')

    def publish(self):
        self.save()
    def __str__(self):
        return self.title



class Student(models.Model):
     application_id = models.AutoField(primary_key=True)
     application_fee = models.IntegerField(blank=True,default=0)
     portal_fee = models.IntegerField(blank=True,default=0)
     late_fee = models.IntegerField(blank=True,default=0)
     total_fee = models.IntegerField(blank=True,default=0)
     name = models.CharField(max_length=100,blank=True)
     fname = models.CharField(max_length=100,blank=True)
     college_name = models.CharField(max_length=100,blank=True)
     branch = models.CharField(max_length=50, blank=True)
     rollno= models.IntegerField(blank=True,default=100)
     year =models.CharField(max_length=50, blank=True)
     sem =models.CharField(max_length=50, blank=True)
     dob = models.DateField()
     session = models.CharField(max_length=50, blank=True)
     stype = models.CharField(max_length=50, blank=True)
     regulartyp = models.CharField(max_length=50, blank=True)
     privatetyp = models.CharField(max_length=50, blank=True)
     payment_status = models.CharField(max_length=50, default='pending')
     def publish(self):
         self.save()

     def __str__(self):
         return self.name
