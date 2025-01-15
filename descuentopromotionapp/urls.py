from django.urls import URLPattern, path
from .views import *

app_name="discprom"

urlpatterns = [
    
    path('', DiscPromList.as_view(), name="home_discprom"),
    path('CRUD/add.html', DiscPromCreate.as_view(), name="discprom_create"),
    path('CRUD/edit.html/<int:pk>', DiscPromEdit.as_view(), name="discprom_edit"),
    path('CRUD/delete.html/<int:pk>', DiscPromDelete.as_view(), name="discprom_delete"),
    
    
]