from django.urls import path
from . import views

app_name="loginapp"

urlpatterns=[
  path('',views.login,name='login')
]