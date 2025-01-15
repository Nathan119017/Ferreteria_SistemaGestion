from django.urls import URLPattern, path
from .views import *

app_name="order_history"

urlpatterns = [
    
    path('', Order_HistoryList.as_view(), name="home_order_history"),
    path('CRUD/add.html', Order_HistoryCreate.as_view(), name="order_history_create"),
    path('CRUD/edit.html/<int:pk>', Order_HistoryEdit.as_view(), name="order_history_edit"),
    path('CRUD/delete.html/<int:pk>', Order_HistoryDelete.as_view(), name="order_history_delete"),
    
]