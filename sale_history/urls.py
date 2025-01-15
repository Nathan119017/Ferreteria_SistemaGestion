from django.urls import URLPattern, path
from .views import *

app_name="sale_history"

urlpatterns = [
    
    path('', Sale_HistoryList.as_view(), name="home_sale_history"),
    path('CRUD/add.html', Sale_HistoryCreate.as_view(), name="sale_history_create"),
    path('CRUD/edit.html/<int:pk>', Sale_HistoryEdit.as_view(), name="sale_history_edit"),
    path('CRUD/delete.html/<int:pk>', Sale_HistoryDelete.as_view(), name="sale_history_delete"),
    
]