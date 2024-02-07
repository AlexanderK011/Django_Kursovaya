from django.shortcuts import render

# Create your views here.
from mysport.models import Brend,Sport_item,Category,Subcat #Subcat_cat

def index(request):
    brends = Brend.objects.all()
    tovars = Sport_item.objects.only('id','name','price','img')[:10]
    cats =  Category.objects.values('id','name')
    subcat = Subcat.objects.only('id','name')
    subc_winter = Subcat.objects.filter(cat__name = 'Зимний спорт').only('name','id')
    subc_adventure = Subcat.objects.filter(cat__name = 'Путешествия').only('name','id')
    obuv = Subcat.objects.filter(name = 'Ботинки').only('name','id')
    odezda = Subcat.objects.filter(name='Одежда').only('name', 'id')
    data ={
        'brends':brends,
        'tovars':tovars,
        'cats':cats,
        'subcat':subcat,
        'subc_winter':subc_winter,
        'subc_adventure':subc_adventure,
        'obuv':obuv,
        'odezda':odezda
    }
    return render(request,'mysport/index.html',data)

def cats(request,id):
    cat_subcat = Subcat.objects.filter(id = id).only('id','name','img_subcatcat')
    brends = Brend.objects.values('id','name')
    cats = Category.objects.values('id', 'name')
    subcat = Subcat.objects.only('id', 'name')
    subc_winter = Subcat.objects.filter(cat__name='Зимний спорт').only('name')
    subc_adventure = Subcat.objects.filter(cat__name='Путешествия').only('name')
    obuv = Subcat.objects.filter(name='Ботинки').only('name', 'id')
    odezda = Subcat.objects.filter(name='Одежда').only('name', 'id')
    data ={
        'cats': cats,
        'subcat': subcat,
        'subc_winter': subc_winter,
        'subc_adventure': subc_adventure,
        'brends': brends,
        'cat_subcat' : cat_subcat,
        'obuv':obuv,
        'odezda':odezda
    }
    return render(request,'mysport/subcategs.html',data)

def tovars(request,id):
    brends = Brend.objects.values('id', 'name')
    cats = Category.objects.values('id', 'name')
    subcat = Subcat.objects.only('id', 'name')
    subc_winter = Subcat.objects.filter(cat__name='Зимний спорт').only('name')
    subc_adventure = Subcat.objects.filter(cat__name='Путешествия').only('name')
    obuv = Subcat.objects.filter(name='Ботинки').only('name', 'id')
    odezda = Subcat.objects.filter(name='Одежда').only('name', 'id')
    tovars = Subcat.objects.filter(id=id).values('subcutscats')
    data = {
        'cats': cats,
        'subcat': subcat,
        'subc_winter': subc_winter,
        'subc_adventure': subc_adventure,
        'brends': brends,
        'obuv': obuv,
        'odezda': odezda,
        'tovars': tovars
    }

    return render(request, 'mysport/tovars.html',data)

def one_tovar(request):
    brends = Brend.objects.values('id', 'name')
    cats = Category.objects.values('id', 'name')
    subcat = Subcat.objects.only('id', 'name')
    subc_winter = Subcat.objects.filter(cat__name='Зимний спорт').only('name')
    subc_adventure = Subcat.objects.filter(cat__name='Путешествия').only('name')
    obuv = Subcat.objects.filter(name='Ботинки').only('name', 'id')
    odezda = Subcat.objects.filter(name='Одежда').only('name', 'id')
    data = {
        'cats': cats,
        'subcat': subcat,
        'subc_winter': subc_winter,
        'subc_adventure': subc_adventure,
        'brends': brends,
        'obuv': obuv,
        'odezda': odezda,
        'tovar':tovar
    }

    return render(request, 'mysport/one_tovar.html',data)

def onas(request):
    brends = Brend.objects.values('id', 'name')
    cats = Category.objects.values('id', 'name')
    subcat = Subcat.objects.only('id', 'name')
    subc_winter = Subcat.objects.filter(cat__name='Зимний спорт').only('name')
    subc_adventure = Subcat.objects.filter(cat__name='Путешествия').only('name')
    obuv = Subcat.objects.filter(name='Ботинки').only('name', 'id')
    odezda = Subcat.objects.filter(name='Одежда').only('name', 'id')
    data = {
        'cats': cats,
        'subcat': subcat,
        'subc_winter': subc_winter,
        'subc_adventure': subc_adventure,
        'brends': brends,
        'obuv': obuv,
        'odezda': odezda
    }

    return render(request, 'mysport/onas.html',data)