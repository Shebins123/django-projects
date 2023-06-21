from django.contrib import admin

from shop.models import category,product

class categoryadmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

admin.site.register(category,categoryadmin)

class productadmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','available','created','updated']
    prepopulated_fields={'slug':('name',)}
admin.site.register(product,productadmin)