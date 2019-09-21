from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime



GENDER_CHOICES = (
    ('Male','Male'),
    ('Female ','Female'),
    ('other','other'),
)


category= (
    ('News','ANNOUNCEMENTS/NOTICES/NEWS'),
    ('Tender ','Tenders'),
    ('Events','EVENTS/WORKSHOPS/CONFERENCES'),
    ('other','other'),
)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    update_type = models.CharField(max_length=20, choices=category, default='News')
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
     mname = models.CharField(max_length=100,blank=True)
     college_name = models.CharField(max_length=100,blank=True)
     eno = models.CharField(max_length=50, blank=True)
     course = models.CharField(max_length=50, blank=True)
     branch = models.CharField(max_length=50, blank=True)
     gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Male')
     rollno= models.IntegerField(blank=True,default=100)
     year =models.CharField(max_length=50, blank=True)
     sem =models.CharField(max_length=50, blank=True)
     dob = models.DateField()
     address=models.CharField(max_length=100,blank=True)
     stype = models.CharField(max_length=50, blank=True)
     sstype = models.CharField(max_length=50, blank=True)
     payment_status = models.CharField(max_length=50, default='pending')
     def publish(self):
         self.save()

     def __str__(self):
         return self.name
