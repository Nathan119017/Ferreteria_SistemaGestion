from django.urls import path
from .views import *

app_name = "cai"

urlpatterns = [
    path('', CAIList.as_view(), name="home_cai"),
    path('CRUD/add.html', CAICreate.as_view(), name="cai_create"),
    path('CRUD/edit.html/<int:pk>', CAIEdit.as_view(), name="cai_edit"),
    path('CRUD/delete.html/<int:pk>', CAIDelete.as_view(), name="cai_delete"),
]