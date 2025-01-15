from django.urls import URLPattern, path
from .views import *

app_name="branch_offices"

urlpatterns = [
    
    path('', Branch_OfficesList.as_view(), name="home_branch_offices"),
    path('CRUD/add.html', Branch_OfficesCreate.as_view(), name="branch_offices_create"),
    path('CRUD/edit.html/<int:pk>', Branch_OfficesEdit.as_view(), name="branch_offices_edit"),
    path('CRUD/delete.html/<int:pk>', Branch_OfficesDelete.as_view(), name="branch_offices_delete"),
    
    
]