from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import booking

# Create your views here.
def register(req):
    if req.method=='POST':
        username=req.POST.get('user')
        email=req.POST.get('email')
        password=req.POST.get('pass')
        cpass=req.POST.get('cpass')
        if password == cpass:
            if User.objects.filter(username=username).exists():
                return redirect("http://127.0.0.1:8000/register/")
            else:
                user_reg=User.objects.create_user(username=username,email=email,password=password)
                user_reg.save()
                return redirect("http://127.0.0.1:8000/")
    return render(req,'req.html')

def sign(req):
    if req.method=='POST':
        email=req.POST.get('uname')
        password=req.POST.get('pass')
        user=auth.authenticate(req,username=email,password=password)
        if user is not None:
            auth.login(req,user)
            return redirect("http://127.0.0.1:8000/")
        else:
            return redirect("http://127.0.0.1:8000/register/")
    return render(req,'l.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def book(req):
    if req.method=="POST":
        form=booking(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    form=booking()
    dict_book={'form':form}
    return render(req,'booking.html',dict_book)

