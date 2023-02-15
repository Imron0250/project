from django.urls import path
from .views import *


urlpatterns = [
    path('Task/', TaskView),  
    path('edit-task/<int:pk>/', edit_task), 
    path('delete-task/<int:pk>/', delete_task), 
    path('task_name/', task_name)

] 