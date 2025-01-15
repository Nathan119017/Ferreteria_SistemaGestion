from django.urls import URLPattern, path
from .views import *

app_name="users"

urlpatterns = [
    
    path('', UsersList.as_view(), name="home_users"),
    path('CRUD/add.html', UsersCreate.as_view(), name="users_create"),
    path('CRUD/edit.html/<int:pk>', UsersEdit.as_view(), name="users_edit"),
    path('CRUD/delete.html/<int:pk>', UsersDelete.as_view(), name="users_delete"),
    
    
]