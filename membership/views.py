from django.shortcuts import render,redirect
from membership.models import *
import stripe
from datetime import datetime, timedelta

def home(request):
    courses = Course.objects.all()
    context = {'courses':courses}
    return render(request,'membership/home.html', context)



def view_course(request, slug):
    course = Course.objects.filter(slug=slug).first()
    course_module = CourseModule.objects.filter(course=course)

    context = {'course': course, 'course_module': course_module}
    return render(request, 'membership/course.html', context)



def become_project1(request): 
    # profile = Membership.objects.filter(user = request.user).first()
    user=request.user
    a = 'M'
    b = True
    c = datetime.now() + timedelta(30)
    d = c
    mem = Membership(user=user, subscription_type=a, is_pro=b, pro_expire_date=d)
    mem.save()
    
    # return redirect("membership/charge/")
    return redirect('charge')

def become_project2(request): 
    # profile = Membership.objects.filter(user = request.user).first()
    user=request.user
    a = 'Y'
    b = True
    c = datetime.now() + timedelta(365)
    d = c
    mem = Membership(user=user, subscription_type=a, is_pro=b, pro_expire_date=d)
    mem.save()
    return redirect('charge1')

def become_pro(request):
    return render(request, 'membership/become_pro.html')

def charge(request):
    profile=Membership.objects.all()
    expiry = datetime.now() + timedelta(30)
    profile.pro_expire_date = expiry
    print('expire date:',expiry)
    return render(request, 'membership/charge.html', {'expiry':expiry})

def charge1(request):
    profile=Membership.objects.all()
    expiry = datetime.now() + timedelta(365)
    profile.pro_expire_date = expiry
    print('expire date:',expiry)
    return render(request, 'membership/charge.html', {'expiry':expiry})




