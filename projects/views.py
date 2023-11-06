from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from projects.models import Project

# Create your views here.
@login_required
def project_list(request):
    projects = Project.objects.filter(owner = request.user)
    context = {
        "project_list": projects,
    }
    return render(request, "projects/list.html", context)

@login_required
def project_detail(request, id):
    details = get_object_or_404(Project, id=id)
    context = {
        "project_detail": details,
     }
    return render(request, "projects/detail.html", context)
