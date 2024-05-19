from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from mysport.models import Brend,Sport_item,Category,Subcat,Characheristic,Color,Size,Order,OrderItem

from mysport.forms import UserRegForm,FeedbackForm,UserPasswordChangeForm,UserUpdateForm,OrderChangeForm

from cart.forms import CartAddProductForm


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
    if request.method == 'POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()
        data = {
            'tovars': tovars,
            'menu': menu,
            'form':form,
            'title': 'Главная'
        }
        return render(request, 'mysport/index.html', data)
    return redirect(index)

def policy_conf(request):
    data = {
        'menu': menu,
        'title': 'Политика конфиденциальности'
    }
    return render(request, 'mysport/policy.html', data)

def polzov_soglas(request):
    data= {
        'menu':menu,
        'title': "Пользовательское соглашение"
    }
    return render(request, 'mysport/polzovatsoglas.html', data)

def haranty_obsluz(request):
    data = {
        'menu': menu,
        'title': "Гарантия обслуживания"
    }
    return render(request, 'mysport/haranty_obsluz.html', data)

def price_haranty(request):
    data= {
        'menu':menu,
        'title': "Гарантия цены"
    }
    return render(request, 'mysport/priceharanty.html', data)

def cats(request,id):
    cat_subcat = Subcat.objects.filter(id = id).only('id','name','img_subcatcat')
    data ={
        'cat_subcat' : cat_subcat,
        'menu': menu,
        'title':'Категории'
    }
    return render(request,'mysport/subcategs.html',data)

def takecategory(request,id):
    cat_subcat = Subcat.objects.filter(cat_id =id)
    data={
        'cat_subcat': cat_subcat,
        'menu': menu,
        'title': 'Подкатегории'
    }
    return render(request,'mysport/subcategs.html',data)


def tovars(request,id):
    tovars = Subcat.objects.filter(id=id).prefetch_related('subcutscats')\
        .values('id','cat','subcutscats','subcutscats__name','subcutscats__id','subcutscats__img',
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
    cart_product_form = CartAddProductForm()
    data = {
        'tovars': tovars,
        'menu':menu,
        'filt_cats':filt_cats,
        'tovars_color':tovars_color,
        'tovars_brends':tovars_brends,
        'subc_id':subcid,
        'subc_name':subc_name,
        'cart_product_form':cart_product_form,
        'title': 'Товары'

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
        'brend_name':brend_name,
        'title': 'Товары'
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

    data = {
        'menu':menu,
        'tovar':tovar,
        'size':size,
        'harakt':harakt,
        'subc':subc,
        'title': tovar.name
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
    if filt_cats1 is None:
        for i in filt_cat:
            filt_cats1.append(i['tree_id'])
            filt_cats = Subcat.objects.filter(tree_id__in = filt_cats1).filter(level=0)
    else:
        filt_cats = Subcat.objects.all()
    data = {
        'results_tovars': results_tovars,
        'menu': menu,
        'query':query,
        'tovars_color': tovars_color,
        'filt_cats': filt_cats,
        'tovars_brends': tovars_brends,
        'title': 'Товары'
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
        'menu':menu,
        'title': 'О нас'
    }

    return render(request, 'mysport/onas.html',data)

def reg(request):
    data = {
        'menu': menu,
        'title': 'Вход'
    }
    if request.method =="POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            messages.success(request,'Аккаунт создан')
            return redirect('index')
    else:
        form = UserRegForm()
        data['form'] = form
        return render(request,'mysport/user/reg.html',data)

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'mysport/user/login.html'
    extra_context = {'menu': menu,'title':'Вход'}

class LogoutUser(LogoutView):
    form_class = AuthenticationForm
    template_name = 'mysport/user/login.html'
    extra_context = {'menu': menu}

@login_required
def profile(request):
    data = {
        'menu': menu,
        'title': 'Профиль'
    }
    return render(request, 'mysport/user/profile.html',data)

@login_required
def order_history(request):
    user_hist = Order.objects.filter(user_id = request.user.id)
    data = {
        'menu': menu,
        'title': 'История заказов',
        'user_hist':user_hist
    }
    return render(request, 'mysport/user/orderhist.html', data)

@login_required
def order_history_items(request,id):
    order = Order.objects.filter(id = id).values('user_id','deny_buy')
    user_hist = OrderItem.objects.filter(order_id = id)
    for i in order:
        if request.user.id == i['user_id'] or request.user.is_staff or request.user.is_moder:
            pass
        else:
            return redirect(profile)
    total = 0
    for i in user_hist:
        total= total + i.get_cost()
    data = {
        'id':id,
        'menu': menu,
        'title': f'Заказ №{id}',
        'user_hist':user_hist,
        'total':total,
        'order':order
    }
    return render(request, 'mysport/user/orderhistitems.html', data)
@login_required
def current_orders(request):
    user_hist = Order.objects.filter(user_id = request.user.id,status__in =['В пути', 'На рассмотрении'],deny_buy=False)
    data = {
        'menu': menu,
        'title': 'История заказов',
        'user_hist':user_hist
    }
    return render(request, 'mysport/user/current_orders.html', data)
@login_required
def user_update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(profile)
    else:
        form = UserUpdateForm(instance = request.user)
        data={
            'form':form,
            'menu':menu,
            'title': f'Изменение профиля'
        }
    return render(request,'mysport/user/profile_update.html',data)

@login_required
def moder(request):
    if request.user.is_moder:
        order = Order.objects.order_by('paid').filter(deny_buy = False)
        data = {
            'menu': menu,
            'order':order,
            'title': f'Управление заказами'
        }
        return render(request, 'mysport/user/acceptmoder_order.html',data)
    else:
        return redirect(profile)

@login_required
def moder_order(request, id):
    if request.user.is_moder:
        order = Order.objects.get(id=id)
        order1 = ''
        order2 = ''
        order3 = ''
        if order.status == 'На рассмотрении':
            order1 ='selected'
        elif order.status == 'В пути':
            order2 = 'selected'
        else:
            order3 = 'selected'
        if order.paid == 'True':
            paid = "Оплачен"
        else:
            paid = "Не оплачен"
        user_hist = OrderItem.objects.filter(order_id=id)
        total = 0
        for i in user_hist:
            total = total + i.get_cost()
        if request.method == 'POST':
            form = OrderChangeForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
                return redirect(moder)
        else:
            form = OrderChangeForm()
            data = {
                'menu': menu,
                'order': order,
                'title': f'Управление Заказом №{id}',
                'user_hist': user_hist,
                'total': total,
                'form':form,
                'id':id,
                'order1':order1,
                'order2':order2,
                'order3':order3,
                'paid':paid
            }
        return render(request, 'mysport/user/moder_order.html', data)
    else:
        return redirect(profile)

class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'mysport/user/change_passw.html'
    success_message = 'Ваш пароль был успешно изменён!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение пароля на сайте'
        context['menu'] = menu
        return context

    def get_success_url(self):
        return reverse_lazy(profile)

