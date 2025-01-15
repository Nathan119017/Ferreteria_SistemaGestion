from django.urls import URLPattern, path
from .views import *

app_name="categories"

urlpatterns = [
    
    path('', CategoriesList.as_view(), name="home_categories"),
    path('CRUD/add.html', CategoriesCreate.as_view(), name="categories_create"),
    path('CRUD/edit.html/<int:pk>', CategoriesEdit.as_view(), name="categories_edit"),
    path('CRUD/delete.html/<int:pk>', CategoriesDelete.as_view(), name="categories_delete"),
    
    
]