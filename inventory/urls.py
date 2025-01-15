from django.urls import URLPattern, path
from .views import *

app_name="inventory"

urlpatterns = [
    
    path('', InventoryList.as_view(), name="home_inventory"),
    path('CRUD/add.html', InventoryCreate.as_view(), name="inventory_create"),
    path('CRUD/edit.html/<int:pk>', InventoryEdit.as_view(), name="inventory_edit"),
    path('CRUD/delete.html/<int:pk>', InventoryDelete.as_view(), name="inventory_delete"),
    
    
]