# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import(
    User,
)
@admin.register(User)
class EmployeeformAdmin(admin.ModelAdmin):
    list_display=['full_name','date_of_joining','mobile_number','alternative_mobile_number','email_id','date_of_birth','gender','marital_status','spouse_name','father_s_name','mother_s_name','permanent_address','corresponding_address','physically_handicapped','blood_group','aadhar_number','upload_aadhar','pan_number','upload_pan','bank_name','confirm_bank_name','bank_account_number','confirm_bank_account_number','bank_IFSC_code','confirm_bank_IFSC_code']