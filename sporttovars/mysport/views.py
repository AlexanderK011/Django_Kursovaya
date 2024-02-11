from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
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

def takecategory(request,id):
    cat_subcat = Subcat.objects.filter(cat_id =id)
    data={
        'cat_subcat': cat_subcat,
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
    tovars_color = Subcat.objects.filter(id=id).values('subcutscats__color', 'subcutscats__color__color','subcutscats__color__id').distinct()
    tovars_brends = Subcat.objects.filter(id=id).values('subcutscats__brend', 'subcutscats__brend__name','subcutscats__brend__id').distinct()
    if request.GET.get('select'):
        ordering = request.GET.get('select')
        tovars = tovars.order_by(ordering)
    for i in filt_cat:
        filt_cats = Subcat.objects.filter(tree_id = i['tree_id']).filter(level=0)
    data = {
        'tovars': tovars,
        'menu':menu,
        'tovar_pricemens':tovar_pricemens,
        'filt_cats':filt_cats,
        'tovars_color':tovars_color,
        'tovars_brends':tovars_brends

    }
    return render(request, 'mysport/tovars.html',data)

def filter_prod(request):
    categories = request.GET.getlist('category[]')
    colors = request.GET.getlist('color[]')
    brends = request.GET.getlist('brends[]')

    # tovars = Subcat.objects.prefetch_related('subcutscats') \
    #     .values('id', 'subcutscats', 'subcutscats__name', 'subcutscats__img',
    #             'subcutscats__color__color', 'subcutscats__price', 'subcutscats__characheristic__country_crator'
    #             , 'subcutscats__characheristic__material','subcutscats__color__id','subcutscats__brend')

    if (len(categories)>0):
        tovars=tovars.filter(id__in = categories).order_by('subcutscats__name').distinct('subcutscats__name')

    if (len(colors)>0):
        print(colors)
        tovars = tovars.filter(subcutscats__color__id__in=colors)
        print(tovars)

    if (len(brends)>0):
        tovars = tovars.filter(subcutscats__brend__in=brends).order_by('subcutscats__name').distinct('subcutscats__name')
        print(brends)
        print(tovars)

    data = render_to_string('mysport/async/tovars_list.html',{'tovars':tovars})
    return JsonResponse({'data':data})


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
    tovars_brend = Sport_item.objects.filter(brend__name = name)
    tovars_color = Sport_item.objects.filter(brend__name = name).values('color','color__color').distinct()
    data = {
        'tovars_brend':tovars_brend,
        'menu':menu,
        'tovars_color':tovars_color
    }
    return render(request, 'mysport/tovars.html',data)

def one_tovar(request,id):
    tovar = Sport_item.objects.get(id=id)
    harakt = Characheristic.objects.get(good=id)
    size = Size.objects.filter(good=id)
    data = {
        'menu':menu,
        'tovar':tovar,
        'size':size,
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