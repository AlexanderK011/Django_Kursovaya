from django.shortcuts import render

# Create your views here.
from mysport.models import Brend,Sport_item,Category,Subcat #Subcat_cat

def index(request):
    brends = Brend.objects.all()
    tovars = Sport_item.objects.all()[:10]
    cats =  Category.objects.values('id','name')
    subcat = Subcat.objects.all()
    # subcat_cat = Subcat_cat.objects.all()
    data ={
        'brends':brends,
        'tovars':tovars,
        'cats':cats,
        'subcat':subcat,
        # 'subcat_cat':subcat_cat
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