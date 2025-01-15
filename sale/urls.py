from django.urls import URLPattern, path
from .views import *
from . import views



app_name="sale"


urlpatterns = [
    
    path('', SaleList.as_view(), name="home_sale"),
    path('CRUD/add.html', SaleCreate.as_view(), name="sale_create"),
    path('CRUD/edit.html/<int:pk>', SaleEdit.as_view(), name="sale_edit"),
    path('CRUD/delete.html/<int:pk>', SaleDelete.as_view(), name="sale_delete"),
    




    
]