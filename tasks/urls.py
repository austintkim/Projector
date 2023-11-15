from django.urls import path
from tasks.views import task_create, task_delete, task_list, task_add_notes

urlpatterns = [
    path("create/<int:project_id>", task_create, name="create_task"),
    path("delete/<int:id>", task_delete, name="delete_task"),
    path("mine/", task_list, name="show_my_tasks"),
    path("add/<int:id>", task_add_notes, name="add_notes")
]
