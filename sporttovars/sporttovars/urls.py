"""
URL configuration for sporttovars project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from mysport.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('subcat/<int:id>/',cats),
    path('subcat/cat/<int:id>/',takecategory,name = 'cat_subc'),
    path('tovars/<int:id>/',tovars, name='tovars'),
    path('policy-confindence/',policy_conf, name='policy_conf'),
    path('price_haranty/',price_haranty, name='price_haranty'),
    path('haranty_obsluz/',haranty_obsluz, name='haranty_obsluz'),
    path('polzov_soglas/',polzov_soglas, name='polzov_soglas'),
    path('one_tovar/<int:id>',one_tovar,name='tovar'),
    path('aboutus/',onas,name='about_us'),
    path('economic/',economic,name='economic'),
    path('tovars/<str:name>/',tovars_brends, name='brend_tovars'),
    path('tovar/search/',search_tovars,name='search'),
    path('filter-products/<int:id>',filter_prod,name='filter_prod'),
    path('filter-products-brend/<str:name>/',filter_prod_brend,name='filter_prod_brend'),
    path('filter-products-search/<str:query>/',filter_search,name='filter_search'),
    path('register/',reg,name = 'reg'),
    path('accounts/profile/',profile,name = 'profile'),
    path('accounts/password-change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/user-update/', user_update_profile, name='user_update'),
    path('accounts/profile/order_history/',order_history,name='hist_ord'),
    path('accounts/profile/current-order',current_orders,name='currentorder'),
    path('accounts/profile/order_history/<int:id>/',order_history_items,name = 'hist_items_order'),
    path('accounts/moder/',moder,name='moder'),
    path('accounts/moder/<int:id>/',moder_order,name='ordermoder'),
    path('login/', LoginUser.as_view(template_name='mysport/user/login.html'), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    re_path(r'^cart/', include(('cart.urls', 'cart'), namespace='cart')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
