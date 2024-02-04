from django.shortcuts import render

# Create your views here.
from mysport.models import Brend,Sport_item



def index(request):
    brends = Brend.objects.all()
    tovars = Sport_item.objects.all()[:10]
    data ={
        'brends':brends,
        'tovars':tovars
    }
    return render(request,'mysport/index.html',data)

def cats(request):
    return render(request,'mysport/subcategs.html')

def tovars(request):
    return render(request, 'mysport/tovars.html')

def one_tovar(request):
    return render(request, 'mysport/one_tovar.html')

def onas(request):
    return render(request, 'mysport/onas.html')