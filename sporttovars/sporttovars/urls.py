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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mysport.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('subcat/<int:id>/',cats),
    path('subcat/cat/<int:id>/',takecategory,name = 'cat_subc'),
    path('tovars/<int:id>/',tovars, name='tovars'),
    path('one_tovar/<int:id>',one_tovar,name='tovar'),
    path('aboutus/',onas,name='about_us'),
    path('tovars/<str:name>/',tovars_brends, name='brend_tovars'),
    path('tovar/search/',search_tovars,name='search'),
    path('tovars/sort/<int:id>/',tovars_sort,name='sort_tovar'),
    path('filter-products/',filter_prod,name='filter_prod')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
