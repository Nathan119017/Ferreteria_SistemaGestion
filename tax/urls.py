from django.urls import path
from .views import *

app_name = "tax"

urlpatterns = [
    path('', TaxList.as_view(), name="home_tax"),
    path('CRUD/add.html', TaxCreate.as_view(), name="tax_create"),
    path('CRUD/edit.html/<int:pk>', TaxEdit.as_view(), name="tax_edit"),
    path('CRUD/delete.html/<int:pk>', TaxDelete.as_view(), name="tax_delete"),
]
