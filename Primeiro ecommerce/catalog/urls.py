


from django.urls import path
from catalog.views import product_list





urlpatterns = [
  path("", product_list,name="product_list" ),

  
]