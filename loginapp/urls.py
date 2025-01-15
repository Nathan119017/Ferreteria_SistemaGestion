from django.urls import path
from . import views

app_name="registerapp"

urlpatterns=[
  path('',views.register,name='register'),
]