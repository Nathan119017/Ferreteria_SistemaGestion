from django.urls import URLPattern, path
from .views import *

app_name="devolucion_history"

urlpatterns = [
    
    path('', Devolucion_HistoryList.as_view(), name="home_devolucion_history"),
    path('CRUD/add.html', Devolucion_HistoryCreate.as_view(), name="devolucion_history_create"),
    path('CRUD/edit.html/<int:pk>', Devolucion_HistoryEdit.as_view(), name="devolucion_history_edit"),
    path('CRUD/delete.html/<int:pk>', Devolucion_HistoryDelete.as_view(), name="devolucion_history_delete"),
    
]