from fileinput import FileInput
from django.core import validators
from django import forms
from .models import User

class DateInput(forms.DateInput):
    input_type='date'


class Employeedetails(forms.ModelForm):
   
    class Meta:
        model=User
        fields=['full_name','date_of_joining','mobile_number','alternative_mobile_number','email_id','date_of_birth','gender','marital_status','spouse_name','father_s_name','mother_s_name','permanent_address','corresponding_address','physically_handicapped','blood_group','aadhar_number','upload_aadhar','pan_number','upload_pan','bank_name','confirm_bank_name','bank_account_number','confirm_bank_account_number','bank_IFSC_code','confirm_bank_IFSC_code']
        widgets={'full_name':forms.TextInput(attrs={'class':'form-control','autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}),'date_of_joining':DateInput(),'mobile_number':forms.NumberInput(attrs={'class':'form-control','pattern':'[0-9]+'}),'alternative_mobile_number':forms.NumberInput(attrs={'class':'form-control','pattern':'[0-9]+'}),'email_id':forms.EmailInput(attrs={'class':'form-control'}),'date_of_birth':DateInput(),'gender':forms.Select(attrs={'class':'form-control'}),'marital_status':forms.Select(attrs={'class':'form-control'}),'spouse_name':forms.TextInput(attrs={'class':'form-control','autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}),'father_s_name':forms.TextInput(attrs={'class':'form-control','autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only'}),'mother_s_name':forms.TextInput(attrs={'class':'form-control','autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}),'permanent_address':forms.TextInput(attrs={'class':'form-control'}),'corresponding_address':forms.TextInput(attrs={'class':'form-control'}),'physically_handicapped':forms.Select(attrs={'class':'form-control'}),'blood_group':forms.Select(attrs={'class':'form-control'}),'aadhar_number':forms.TextInput(attrs={'class':'form-control'}),'upload_aadhar':forms.FileInput(),'pan_number':forms.TextInput(attrs={'class':'form-control'}),'upload_pan':forms.FileInput(),'bank_name':forms.TextInput(attrs={'class':'form-control','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}),'confirm_bank_name':forms.TextInput(attrs={'class':'form-control','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}),'bank_account_number':forms.NumberInput(attrs={'class':'form-control'}),'confirm_bank_account_number':forms.NumberInput(attrs={'class':'form-control'}),'bank_IFSC_code':forms.TextInput(attrs={'class':'form-control'}),'confirm_bank_IFSC_code':forms.TextInput(attrs={'class':'form-control'})}
    def clean(self):
        cleaned_data = self.cleaned_data # individual field's clean methods have already been called
        mobile_number=cleaned_data.get("mobile_number")
        dd=str(mobile_number)
        #d=dd[0]
       

        



        full_name=cleaned_data.get("full_name")
        date_of_birth=cleaned_data.get("date_of_birth")
        z=str(date_of_birth)
        dt=z.replace("-","/")
        dob=dt[8]+dt[9]+"/"+dt[5]+dt[6]+"/"+dt[0]+dt[1]+dt[2]+dt[3]
        aadhar_number=cleaned_data.get("aadhar_number")

        aadhar_number=cleaned_data.get("aadhar_number")
        a=str(aadhar_number)
        upload_aadhar=cleaned_data.get("upload_aadhar")
        pan_number=cleaned_data.get("pan_number")
        upload_pan=cleaned_data.get("upload_pan")
        
     
        bank_name = cleaned_data.get("bank_name")
        confirm_bank_name = cleaned_data.get("confirm_bank_name")
        bank_account_number=cleaned_data.get("bank_account_number")
        confirm_bank_account_number=cleaned_data.get("confirm_bank_account_number")
        ban=str(bank_account_number)
        bank_IFSC_code=cleaned_data.get("bank_IFSC_code")
        confirm_bank_IFSC_code=cleaned_data.get("confirm_bank_IFSC_code")
       
      
        if len(a)<14 or len(a)>14:
            raise forms.ValidationError("Please give correct aadhar number")

        if len(bank_IFSC_code)<11 or len(bank_IFSC_code)>11:
            raise forms.ValidationError("Please give correct bank_IFSC_code")    
        if len(pan_number)<10 or len(pan_number)>10:
            raise forms.ValidationError("Please give correct pan number")    
        if len(ban)<9 or len(ban)>18:
            raise forms.ValidationError("bank account number must be of 9-18 character")
        if bank_name != confirm_bank_name :
            raise forms.ValidationError("Bank name must be identical.")
        if bank_account_number!=confirm_bank_account_number:
            raise forms.ValidationError("bank account number must be identical.")
        if bank_IFSC_code!=confirm_bank_IFSC_code:
            raise forms.ValidationError("Bank IFSC code must be identical.")
        if len(dd)<10 or len(dd)>10:
           raise forms.ValidationError("mobile no must be of 10 digit") 
        #if d:
           # raise forms.ValidationError("first digit of the mobile no must be between [1-9]") 


       

        import pytesseract as tess,re

        tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        from PIL import Image
        img1 = Image.open(upload_aadhar)
        img2 = Image.open(upload_pan)
        text1=tess.image_to_string(img1)
        text2=tess.image_to_string(img2)



        

        if full_name not in text1:
            raise forms.ValidationError("aadhar name is not matched with full name.")
        if aadhar_number not in text1:
            raise forms.ValidationError("aadhar number is not matched with your aadhar data.")    
        if dob not in text1:
            raise forms.ValidationError("Date of birth is not matched with your aadhar data.") 
        if pan_number not in text2:
            raise forms.ValidationError("You have uploaded another document instead of pan card")



        return cleaned_data  




   
         