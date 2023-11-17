from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tasks.models import Project, Task
from tasks.forms import TaskForm, NotesForm


# Create your views here.
@login_required
def task_list(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "task_list": tasks,
    }
    return render(request, "tasks/list.html", context)


@login_required
def task_create(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(False)
            task.save()
            task.project = project
            task.save()
            return redirect("show_project", id=project.id)
    else:
        form = TaskForm()
    context = {"form": form}
    return render(request, "tasks/create.html", context)

@login_required
def task_edit(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("show_project", id=task.project.id)
    else:
        form = TaskForm(instance=task)
        context = {
            "form": form,
        }
        return render(request, "tasks/edit.html", context)

@login_required
def project_detail(request, id):
    details = get_object_or_404(Project, id=id)
    context = {
        "project_detail": details,
    }
    return render(request, "projects/detail.html", context)

@login_required
def task_add_notes(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = NotesForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")
    else:
        form = NotesForm(instance=task)
        context = {
            "form": form,
        }
        return render(request, "tasks/add_notes.html", context)

@login_required
def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
       task.delete()
       return redirect("show_project", id=task.project.id)

    return render(request, "tasks/delete.html")
