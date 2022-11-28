from email import message
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Member
from django.db.models import Q

def index(request):
    return render(request,'home.html')


def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect("register")
        return redirect('/')


    else:
        return render(request,'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('new')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect("/")


def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect('new')


def update(request, id):
  mem=Member.objects.get(id=id)
  return render(request,'update.html',{'mem':mem})


def addrec(request):
  x = request.POST['first']
  y = request.POST['last']
  z=request.POST['country']
  member = Member(firstname=x, lastname=y, country=z)
  member.save()
  return redirect('new')

def add(request):
  return render(request,'add.html')



def new(request):
    if 'q' in request.GET:
        q=request.GET['q']
        #mem=Member.objects.filter(firstname__icontains=q)
        multiple_q=Q(Q(firstname__icontains=q) | Q(lastname__icontains=q))
        mem=Member.objects.filter(multiple_q)
    else:
        mem=Member.objects.all()
    context={
        'mem':mem
    }
    return render(request,'newpage.html',context)

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z
    mem.save()
    return redirect("new")







