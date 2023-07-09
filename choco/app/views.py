from django.shortcuts import render,redirect
from .models import chocolate


# Create your views here.
def index(request):
    dict_product={
        'cho':chocolate.objects.all()
        }
    return render(request,'index.html', dict_product)

def about(req):
    return render(req,'about.html')

def chocolates(req):
    dict_prodc={'cho':chocolate.objects.all()}
    return render(req,'chocolate.html',dict_prodc)

