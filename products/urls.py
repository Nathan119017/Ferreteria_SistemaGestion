from django.urls import URLPattern, path
from .views import *

app_name="products"

urlpatterns = [
    
    path('', ProductsList.as_view(), name="home_products"),
    path('CRUD/add.html', ProductsCreate.as_view(), name="products_create"),
    path('CRUD/edit.html/<int:pk>', ProductsEdit.as_view(), name="products_edit"),
    path('CRUD/delete.html/<int:pk>', ProductsDelete.as_view(), name="products_delete"),
    
    
]