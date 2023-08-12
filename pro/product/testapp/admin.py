from django.contrib import admin
from .models import Combinedata
# Register your models here.
class ComBineDataAdmin(admin.ModelAdmin):
    list_display = ('id','customer_id','pack1','pack2' )

admin.site.register(Combinedata,ComBineDataAdmin)