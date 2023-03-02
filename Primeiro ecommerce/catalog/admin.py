from django.contrib import admin

# Register your models here.

from .models import Product,Category

#personalizar a classe
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","slug", "created","modified"]
    search_fields = ["name","slug"]
    list_filter = ["created","modified"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","slug","category","created","modified","price"]
    search_fields = ["name","slug","category__name"]#pesquisar pelo nome da categoria
    list_filter = ["created","modified"]
    

#Permitindo que o cadastro tenha o admin
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
