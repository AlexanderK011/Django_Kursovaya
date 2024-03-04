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
        .values('id','cat','subcutscats','subcutscats__name','subcutscats__img',
                'subcutscats__color__color','subcutscats__price','subcutscats__characheristic__country_crator'
                ,'subcutscats__characheristic__material')
    subc_name = Subcat.objects.filter(id=id).values('name')
    for i in subc_name:
        subc_name = i
    subcid = tovars[0]['cat']
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
        'filt_cats':filt_cats,
        'tovars_color':tovars_color,
        'tovars_brends':tovars_brends,
        'subc_id':subcid,
        'subc_name':subc_name

    }
    return render(request, 'mysport/tovars.html',data)

def filter_prod(request,id):
    categories = request.GET.getlist('category[]')
    colors = request.GET.getlist('color[]')
    brends = request.GET.getlist('brends[]')

    tovars = Sport_item.objects.filter(subcat__cat__id=id).order_by('name').distinct('name')

    min_price = request.GET['min_price']
    max_price = request.GET['max_price']
    tovars = tovars.filter(price__gte = min_price)
    tovars = tovars.filter(price__lte= max_price)

    # tovars = Subcat.objects.filter(cat=id).prefetch_related('subcutscats') \
    #     .values('id', 'subcutscats', 'subcutscats__name', 'subcutscats__img',
    #             'subcutscats__color__color', 'subcutscats__price', 'subcutscats__characheristic__country_crator'
    #             , 'subcutscats__characheristic__material','subcutscats__color__id','subcutscats__brend').order_by('subcutscats__name').distinct('subcutscats__name')

    if (len(categories)>0):
        tovars=tovars.filter(subcat__id__in = categories).order_by('name').distinct('name')

    if (len(colors)>0):
        tovars = tovars.filter(color__id__in=colors)

    if (len(brends)>0):
        tovars = tovars.filter(brend__in=brends).order_by('name').distinct('name')

    data = render_to_string('mysport/async/tovars_list.html',{'tovars':tovars})
    return JsonResponse({'data':data})


def tovars_brends(request,name):
    tovars_brend = Sport_item.objects.filter(brend__name = name)
    filt_cat = Subcat.objects.filter(subcutscats__brend__name=name).values('tree_id')
    tovars_color = Sport_item.objects.filter(brend__name = name).values('color','color__color').distinct()
    tovars_brends = Subcat.objects.filter(subcutscats__brend__name=name).values('subcutscats__brend', 'subcutscats__brend__name',
                                                        'subcutscats__brend__id').order_by('subcutscats__brend__name').distinct('subcutscats__brend__name')

    if request.GET.get('select'):
        ordering = request.GET.get('select')
        tovars_brend = tovars_brend.order_by(ordering)
    brend_name = name
    for i in filt_cat:
        filt_cats = Subcat.objects.filter(tree_id = i['tree_id']).filter(level=0)
    data = {
        'tovars_brend':tovars_brend,
        'menu':menu,
        'tovars_color':tovars_color,
        'filt_cats': filt_cats,
        'tovars_brends':tovars_brends,
        'brend_name':brend_name
    }
    return render(request, 'mysport/tovars.html',data)

def filter_prod_brend(request,name):
    categories = request.GET.getlist('category[]')
    colors = request.GET.getlist('color[]')
    tovars = Sport_item.objects.filter(brend__name=name).order_by('name').distinct('name')

    min_price = request.GET['min_price']
    max_price = request.GET['max_price']
    tovars = tovars.filter(price__gte=min_price)
    tovars = tovars.filter(price__lte=max_price)

    if (len(categories)>0):
        tovars=tovars.filter(subcat__id__in = categories).order_by('name').distinct('name')

    if (len(colors)>0):
        tovars = tovars.filter(color__id__in=colors).order_by('name').distinct('name')


    data = render_to_string('mysport/async/tovars_list.html',{'tovars':tovars})
    return JsonResponse({'data':data})

def one_tovar(request,id):
    tovar = Sport_item.objects.get(id=id)
    subc = Subcat.objects.filter(subcutscats__id = id).values('name','id')[:1]
    for i in subc:
        subc = i
    harakt = Characheristic.objects.get(good=id)
    size = Size.objects.filter(good__id=id)
    print(size)
    data = {
        'menu':menu,
        'tovar':tovar,
        'size':size,
        'harakt':harakt,
        'subc':subc
    }
    return render(request, 'mysport/one_tovar.html',data)

def search_tovars(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        if query == '':
            query = 'none'
    results_tovars = Sport_item.objects.filter(Q(name__icontains=query)|Q(brend__name__icontains=query)).all()

    if not Subcat.objects.filter(subcutscats__name__icontains=query):
        filt_cat = Subcat.objects.filter(subcutscats__brend__name__icontains=query).values('tree_id')
    else:
        filt_cat = Subcat.objects.filter(subcutscats__name__icontains=query).values('tree_id')
    if not Sport_item.objects.filter(name__icontains=query).values('color', 'color__color').distinct():
        tovars_color = Sport_item.objects.filter(brend__name__icontains=query).values('color', 'color__color').distinct()
    else:
        tovars_color = Sport_item.objects.filter(name__icontains=query).values('color',
                                                                                      'color__color').distinct()
    tovars_brends = Subcat.objects.filter(subcutscats__name__icontains=query).values('subcutscats__brend',
                                                                                'subcutscats__brend__name',
                                                                                'subcutscats__brend__id').order_by(
        'subcutscats__brend__name').distinct('subcutscats__brend__name')
    filt_cats1 = []
    for i in filt_cat:
        filt_cats1.append(i['tree_id'])
        filt_cats = Subcat.objects.filter(tree_id__in = filt_cats1).filter(level=0)
    data = {
        'results_tovars': results_tovars,
        'menu': menu,
        'query':query,
        'tovars_color': tovars_color,
        'filt_cats': filt_cats,
        'tovars_brends': tovars_brends,
    }
    return render(request,'mysport/tovars.html',data)

def filter_search(request,query):
    categories = request.GET.getlist('category[]')
    colors = request.GET.getlist('color[]')
    brends = request.GET.getlist('brends[]')
    tovars = Sport_item.objects.filter(Q(name__icontains=query)|Q(brend__name__icontains=query)).order_by('name').distinct('name')

    min_price = request.GET['min_price']
    max_price = request.GET['max_price']

    tovars = tovars.filter(price__gte=min_price)
    tovars = tovars.filter(price__lte=max_price)

    if (len(categories) > 0):
        tovars = tovars.filter(subcat__id__in=categories).order_by('name').distinct('name')

    if (len(colors) > 0):
        tovars = tovars.filter(color__id__in=colors)

    if (len(brends) > 0):
        tovars = tovars.filter(brend__in=brends).order_by('name').distinct('name')


    data = render_to_string('mysport/async/tovars_list.html',{'tovars':tovars})
    return JsonResponse({'data':data})

def onas(request):
    data = {
        'menu':menu
    }

    return render(request, 'mysport/onas.html',data)