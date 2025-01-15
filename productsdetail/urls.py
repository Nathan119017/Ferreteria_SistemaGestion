from django.urls import URLPattern, path
from .views import *

app_name="productsdetail"

urlpatterns = [
    
    path('', ProductsDetailList.as_view(), name="home_productsdetail"),
    path('CRUD/add.html', ProductsDetailCreate.as_view(), name="productsdetail_create"),
    path('CRUD/edit.html/<int:pk>', ProductsDetailEdit.as_view(), name="productsdetail_edit"),
    path('CRUD/delete.html/<int:pk>', ProductsDetailDelete.as_view(), name="productsdetail_delete"),
    
    
]