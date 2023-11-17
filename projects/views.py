from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from projects.models import Project
from projects.forms import ProjectForm
from django.db.models import Q


# Create your views here.
@login_required
def project_list(request):
    projects = Project.objects.filter(Q(owner=request.user)|Q(team_member=request.user)).distinct()
    print('projects', projects)
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


@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            # created_project_id = project.id

            team_members = request.POST.getlist('team_member')

            for member in team_members:
                project.team_member.add(int(member))

            return redirect("list_projects")
    else:
        form = ProjectForm(user=request.user)
    context = {"form": form}
    return render(request, "projects/create.html", context)

@login_required
def project_edit(request, id):
    print("edit project request", request.POST)
    project = Project.objects.get(id=id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = ProjectForm(instance=project, user=request.user)
    context = {
            "form": form,
        }
    return render(request, "projects/edit.html", context)

@login_required
def project_delete(request, id):
    project_id = Project.objects.get(id=id)
    if request.method == "POST":
        project_id.delete()
        return redirect("list_projects")

    return render(request, "projects/delete.html")
