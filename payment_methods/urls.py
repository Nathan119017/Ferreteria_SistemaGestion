from django.urls import URLPattern, path
from .views import *

app_name="payment_methods"

urlpatterns = [
    
    path('', Payment_MethodsList.as_view(), name="home_payment_methods"),
    path('CRUD/add.html', Payment_MethodsCreate.as_view(), name="payment_methods_create"),
    path('CRUD/edit.html/<int:pk>', Payment_MethodsEdit.as_view(), name="payment_methods_edit"),
    path('CRUD/delete.html/<int:pk>', Payment_MethodsDelete.as_view(), name="payment_methods_delete"),
    
    
]