from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from mysport.models import Brend,Sport_item,Category,Subcat,Characheristic,Color,Size #Subcat_cat

menu = {
    'brends' : Brend.objects.all(),
    'cats' :  Category.objects.values('id','name'),
    'subcat' : Subcat.objects.only('id','name'),
    'subc_winter' : Subcat.objects.filter(cat__name = 'Зимний спорт').only('name','id'),
    'subc_adventure' : Subcat.objects.filter(cat__name = 'Путешествия').only('name','id'),
    'obuv' : Subcat.objects.filter(name = 'Ботинки').only('name','id'),
    "odezda" : Subcat.objects.filter(name='Одежда').only('name', 'id'),
}

def index(request):
    tovars = Sport_item.objects.only('id', 'name', 'price', 'img')[:10]
    data={
        'tovars':tovars,
        'menu':menu,
    }

    return render(request,'mysport/index.html',data)

def cats(request,id):
    cat_subcat = Subcat.objects.filter(id = id).only('id','name','img_subcatcat')
    data ={
         'cat_subcat' : cat_subcat,
        'menu': menu,
    }
    return render(request,'mysport/subcategs.html',data)

def tovars(request,id):
    tovars = Subcat.objects.filter(id=id).prefetch_related('subcutscats')\
        .values('id','subcutscats','subcutscats__name','subcutscats__img',
                'subcutscats__color__color','subcutscats__price','subcutscats__characheristic__country_crator'
                ,'subcutscats__characheristic__material')
    tovar_pricemens = tovars.order_by('subcutscats__price')
    filt_cat = Subcat.objects.filter(id = id).values('tree_id')
    for i in filt_cat:
        filt_cats = Subcat.objects.filter(tree_id = i['tree_id']).filter(level=0)


    data = {
        'tovars': tovars,
        'menu':menu,
        'tovar_pricemens':tovar_pricemens,
        'filt_cats':filt_cats

    }
    return render(request, 'mysport/tovars.html',data)

def tovars_sort(request,id):
    current_id = id
    tovars = Subcat.objects.filter(id=id).prefetch_related('subcutscats')\
        .values('id','subcutscats','subcutscats__name','subcutscats__img',
                'subcutscats__color__color','subcutscats__price','subcutscats__characheristic__country_crator'
                ,'subcutscats__characheristic__material')
    tovars = tovars.order_by('subcutscats__price')
    data = {
        'menu':menu,
        'tovars':tovars,
        'current_id':current_id
    }
    return render(request, 'mysport/tovars.html', data)

def tovars_brends(request,name):
    tovars_brend = Sport_item.objects.select_related('characheristic__good').filter(brend__name = name)
    data = {
        'tovars_brend':tovars_brend,
        'menu':menu
    }
    return render(request, 'mysport/tovars.html',data)

def one_tovar(request,id):
    tovar = Sport_item.objects.get(id=id)
    harakt = Characheristic.objects.get(good=id)
    color = Color.objects.get(good=id)
    size = Size.objects.filter(good=id)
    data = {
        'menu':menu,
        'tovar':tovar,
        'size':size,
        'color':color,
        'harakt':harakt
    }
    return render(request, 'mysport/one_tovar.html',data)

def search_tovars(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        if query == '':
            query = 'none'
    results_tovars = Sport_item.objects.filter(Q(name__icontains=query)|Q(brend__name__icontains=query)).all()
    data = {
        'results_tovars': results_tovars,
        'menu': menu,
        'query':query,
    }
    return render(request,'mysport/tovars.html',data)

def onas(request):
    data = {
        'menu':menu
    }

    return render(request, 'mysport/onas.html',data)