
# Create your models here.
from django.core.validators import MaxValueValidator,MinValueValidator
from django import forms
from django.db import models


GENDER_CHOICES=(
    ("Male","Male"),
    ("Female","Female")
)

MARITAL_STATUS_CHOICES=( 
    ("Married","Married"),
    ("Unmarried","Unmarried"),
    ("Divorce","Divorce"),
    ("Widow","Widow")

)
BLOOD_GROUP_CHOICES=( 
    ("A+","A+"),
    ("A-","A-"),
    ("B+","B+"),
    ("B-","B-"),
    ("AB+","AB+"),
    ("AB-","AB-"),
    ("O+","O+"),
    ("O-","O-")
)
PHYSICALLY_HANDICAPPED_CHOICES=(
    ("Yes","Yes"),
    ("No","No")
)
class User(models.Model):
    full_name=models.CharField(max_length=50)
    date_of_joining=models.DateTimeField()
    mobile_number=models.CharField(max_length=10)
    alternative_mobile_number=models.CharField(max_length=10)
    email_id=models.CharField(max_length=30)
    date_of_birth=models.DateTimeField()
    gender=models.CharField(choices=GENDER_CHOICES,max_length=6)
    marital_status=models.CharField(choices=MARITAL_STATUS_CHOICES,max_length=9)
    spouse_name=models.CharField(max_length=50)
    father_s_name=models.CharField(max_length=50)
    mother_s_name=models.CharField(max_length=50)
    permanent_address=models.CharField(max_length=1000)
    corresponding_address=models.CharField(max_length=1000)
    physically_handicapped=models.CharField(choices=PHYSICALLY_HANDICAPPED_CHOICES, max_length=3)
    blood_group=models.CharField(choices=BLOOD_GROUP_CHOICES,max_length=6)
    aadhar_number=models.TextField(max_length=14)
    upload_aadhar= models.ImageField(upload_to='uploads/')
    pan_number=models.CharField(max_length=10)
    upload_pan= models.ImageField(upload_to='uploads/')
    bank_name=models.CharField(max_length=30)
    confirm_bank_name=models.CharField(max_length=30)
    bank_account_number=models.IntegerField()
    confirm_bank_account_number=models.IntegerField()
    bank_IFSC_code=models.CharField(max_length=18)
    confirm_bank_IFSC_code=models.CharField(max_length=11)


def __str__(self):
    return self.full_name

