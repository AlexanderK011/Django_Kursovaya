from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *
# Register your models here.

admin.site.register(Brend)
admin.site.register(Sport_item)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Characheristic)
admin.site.register(Category)
# admin.site.register(Subcat)
admin.site.register(Subcat,MPTTModelAdmin)
# admin.site.register(Subcat_cat)
