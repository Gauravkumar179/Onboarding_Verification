from django.shortcuts import render
from .forms import Employeedetails
from django import forms
from django.contrib import messages

# Create your views here.





def showformdata(request):
    if request.method=='POST':
        form=Employeedetails(request.POST or None,request.FILES)
        if form.is_valid():
             if 'upload_aadhar' and 'upload_pan' in request.FILES:
                form.upload_aadhar = request.FILES['upload_aadhar']
                form.upload_pan=request.FILES['upload_pan']
                form.save()
                messages.success(request,'Congratulations!! You have submitted your details Successfully')

                

    else:

        form=Employeedetails()
    return render(request,'Employee/createform.html',{'form':form})
