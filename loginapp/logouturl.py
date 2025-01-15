from django.urls import path
from . import views

app_name="logoutapp"

urlpatterns=[
  path('',views.logout,name='logout')
]