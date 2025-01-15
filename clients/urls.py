from django.urls import URLPattern, path
from .views import *

app_name="clients"

urlpatterns = [
    
    path('', ClientsList.as_view(), name="home_clients"),
    path('CRUD/add.html', ClientsCreate.as_view(), name="clients_create"),
    path('CRUD/edit.html/<int:pk>', ClientsEdit.as_view(), name="clients_edit"),
    path('CRUD/delete.html/<int:pk>', ClientsDelete.as_view(), name="clients_delete"),
    
    
]