from django.urls import URLPattern, path
from .views import *

app_name="tax_history"

urlpatterns = [
    
    path('', Tax_HistoryList.as_view(), name="home_tax_history"),
    path('CRUD/add.html', Tax_HistoryCreate.as_view(), name="tax_history_create"),
    path('CRUD/edit.html/<int:pk>', Tax_HistoryEdit.as_view(), name="tax_history_edit"),
    path('CRUD/delete.html/<int:pk>', Tax_HistoryDelete.as_view(), name="tax_history_delete"),
    
]