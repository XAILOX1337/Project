from django.contrib import admin
from .models import xailox
from django.utils import timezone
from django.utils.html import format_html 
# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ['id','title', 'description','price','created_date','updated_date','auction','image_thumb']
    list_filter = ['price','created_at','auction']
    actions = ['make_auction_as_false','make_auction_as_true']
    
    
    def image_thumb(self, obj):

        return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))

    image_thumb.short_description = 'изображение'

    @admin.action(description='- Торг(Не для кавказцев)')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
    
    @admin.action(description='+ Торг(Для кавказцев)')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
    
    fieldsets = (('Общее',{'fields':('title','description','image')}),
                 ('Финансы',{'fields':('price','auction'),'classes':['collapse']}))

admin.site.register(xailox, Admin)