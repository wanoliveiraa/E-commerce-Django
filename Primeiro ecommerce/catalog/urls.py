
#apenas das aplicações 

from django.urls import path
from catalog.views import product_list,category





urlpatterns = [
  path("", product_list,name="product_list" ),
 path("<str:category_slug>/",category,name="category"),#url amigavel parametrizada
]