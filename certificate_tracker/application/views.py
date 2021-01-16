from django.shortcuts import render
from .models import Sin1

# Create your views here.

def index(request):
    return render(request,"index.html",{})

def sin1(request):
    data = Sin1.objects.all()
    return render(request,"sin1.html",{'data':data})
