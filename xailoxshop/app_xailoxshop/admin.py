from django.contrib import admin
from .models import xailox
from django.utils import timezone
# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ['id','title', 'description','price','created_date','updated_date','auction']
    list_filter = ['price','created_at','auction']
    actions = ['make_auction_as_false','make_auction_as_true']
     
    

    @admin.action(description='- Торг(Не для кавказцев)')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
    
    @admin.action(description='+ Торг(Для кавказцев)')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
    
    fieldsets = (('Общее',{'fields':('title','description')}),('Финансы',{'fields':('price','auction'),'classes':['collapse']}))

admin.site.register(xailox, Admin)