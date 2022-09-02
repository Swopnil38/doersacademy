from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from homepage.models import intrested_applicant,emaillist
from django.contrib import messages


def InsertDetails(request):
    if request.method=='POST':
        if request.POST.get('email_address'):
            savedetails = emaillist()
            savedetails.email=request.POST.get('email_address')
            savedetails.save()
            messages.success(request,'Details Has been Successfully Added')
            return render(request,'index.html')
    else:
    	    return render(request,'index.html')
    
def course(request):
    
    return render(request,'course.html')
    

def form(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('plan') and request.POST.get('yes/no') :
            savedetails = intrested_applicant()
            savedetails.applicant_name=request.POST.get('name')
            savedetails.applicant_phone=request.POST.get('phone')
            savedetails.applicant_email=request.POST.get('email')
            savedetails.applicant_course=request.POST.get('plan')
            savedetails.applicant_willingness=request.POST.get('yes/no')
            savedetails.save()
            messages.success(request,'Details Has been Successfully Added')
            return render(request,'index.html')
        
    else:
        return render(request,'form.html')

