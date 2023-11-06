from django.shortcuts import render, redirect
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
