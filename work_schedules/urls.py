from django.urls import URLPattern, path
from .views import *

app_name="work_schedules"

urlpatterns = [
    
    path('', Work_SchedulesList.as_view(), name="home_work_schedules"),
    path('CRUD/add.html', Work_SchedulesCreate.as_view(), name="work_schedules_create"),
    path('CRUD/edit.html/<int:pk>', Work_SchedulesEdit.as_view(), name="work_schedules_edit"),
    path('CRUD/delete.html/<int:pk>', Work_SchedulesDelete.as_view(), name="work_schedules_delete"),
    
    
]