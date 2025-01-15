from django.urls import URLPattern, path
from .views import *

app_name="suppliers"

urlpatterns = [
    
    path('', SuppliersList.as_view(), name="home_suppliers"),
    path('CRUD/add.html', SuppliersCreate.as_view(), name="suppliers_create"),
    path('CRUD/edit.html/<int:pk>', SuppliersEdit.as_view(), name="suppliers_edit"),
    path('CRUD/delete.html/<int:pk>', SuppliersDelete.as_view(), name="suppliers_delete"),
    
    
]