from django.urls import URLPattern, path
from .views import *

app_name="orderdetail"

urlpatterns = [
  
  path('', OrderDetailList.as_view(), name="home_orderdetail"),
  path('CRUD/add.html', OrderDetailCreate.as_view(), name="orderdetail_create"),
  path('CRUD/edit.html/<int:pk>', OrderDetailEdit.as_view(), name="orderdetail_edit"),
  path('CRUD/delete.html/<int:pk>', OrderDetailDelete.as_view(), name="orderdetail_delete"),

    
]