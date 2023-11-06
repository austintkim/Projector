from django.urls import path
from tasks.views import task_create, task_list

urlpatterns = [
    path("create/", task_create, name="create_task"),
    path("mine/", task_list, name="show_my_tasks" )
]
