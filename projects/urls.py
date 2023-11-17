from django.urls import path
from projects.views import project_list, project_detail, project_create, project_edit, project_delete

urlpatterns = [
    path("", project_list, name="list_projects"),
    path("<int:id>/", project_detail, name="show_project"),
    path("create/", project_create, name="create_project"),
    path("delete/<int:id>", project_delete, name="delete_project"),
    path("edit/<int:id>/", project_edit, name="edit_project")
]
