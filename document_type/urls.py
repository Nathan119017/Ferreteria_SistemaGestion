from django.urls import URLPattern, path
from .views import *

app_name="document_type"

urlpatterns = [
    
    path('', Document_TypeList.as_view(), name="home_document_type"),
    path('CRUD/add.html', Document_TypeCreate.as_view(), name="document_type_create"),
    path('CRUD/edit.html/<int:pk>', Document_TypeEdit.as_view(), name="document_type_edit"),
    path('CRUD/delete.html/<int:pk>', Document_TypeDelete.as_view(), name="document_type_delete"),
    
]