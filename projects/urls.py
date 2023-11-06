from django.urls import path
from projects.views import project_list, project_detail

urlpatterns = [
    path("", project_list, name = "list_projects"),
    path("<int:id>/", project_detail, name = "show_project"),
]
