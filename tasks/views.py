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
            task.project.add(project)
            task.save()
            task.assignee = request.user
            task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {"form": form}
    return render(request, "tasks/create.html", context)

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
        return render(request, "tasks/edit.html", context)

@login_required
def task_delete(request, id):
    task_id = Task.objects.get(id=id)
    if request.method == "POST":
       task_id.delete()
       return redirect("show_my_tasks")

    return render(request, "tasks/delete.html")
