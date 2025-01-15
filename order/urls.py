from django.urls import URLPattern, path
from .views import *

app_name="order"

urlpatterns = [
  
  path('', OrderList.as_view(), name="home_order"),
  path('CRUD/add.html', OrderCreate.as_view(), name="order_create"),
  path('CRUD/edit.html/<int:pk>', OrderEdit.as_view(), name="order_edit"),
  path('CRUD/delete.html/<int:pk>', OrderDelete.as_view(), name="order_delete"),

    
]