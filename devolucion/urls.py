from django.urls import path
from .views import *

app_name = "devolucion"

urlpatterns = [
    path('', DevolucionList.as_view(), name="home_devolucion"),
    path('CRUD/add.html', DevolucionCreate.as_view(), name="devolucion_create"),
    path('CRUD/edit.html/<int:pk>', DevolucionEdit.as_view(), name="devolucion_edit"),
    path('CRUD/delete.html/<int:pk>', DevolucionDelete.as_view(), name="devolucion_delete"),
]
