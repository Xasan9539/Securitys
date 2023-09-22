from django.shortcuts import render
from .models import Security
from .models import About
# Create your views here.
def test(request):
    return render(request,'mainapp/test.html')

def index(request):
    return render(request,'mainapp/index.html')

def guard(request):
    securitys = Security.objects.all()

    context = {
        "securitys":securitys
    }
    return render(request,'mainapp/guard.html',context)


def about(request):
    abouts = About.objects.all()

    context = {
        "abouts":abouts
    }
    return render(request,'mainapp/about.html',context)