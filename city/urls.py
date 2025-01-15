from django.urls import path
from .views import *

app_name = "city"  # Cambio de 'tax' a 'city' según el modelo

urlpatterns = [
    path('', CityList.as_view(), name="home_city"),  # Cambio de 'home_tax' a 'home_city'
    path('CRUD/add.html', CityCreate.as_view(), name="city_create"),  # Cambio de 'tax_create' a 'city_create'
    path('CRUD/edit.html/<int:pk>', CityEdit.as_view(), name="city_edit"),  # Cambio de 'tax_edit' a 'city_edit'
    path('CRUD/delete.html/<int:pk>', CityDelete.as_view(), name="city_delete"),  # Cambio de 'tax_delete' a 'city_delete'
]
