from django.urls import URLPattern, path
from .views import *

app_name="products_history"

urlpatterns = [
    
    path('', Products_HistoryList.as_view(), name="home_products_history"),
    path('CRUD/add.html', Products_HistoryCreate.as_view(), name="products_history_create"),
    path('CRUD/edit.html/<int:pk>', Products_HistoryEdit.as_view(), name="products_history_edit"),
    path('CRUD/delete.html/<int:pk>', Products_HistoryDelete.as_view(), name="products_history_delete"),
    
]