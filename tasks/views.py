from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from tasks.forms import TaskForm


# Create your views here.
@login_required
def task_list(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "task_list": tasks,
    }
    return render(request, "tasks/list.html", context)


@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(False)
            task.owner = request.user
            task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {"form": form}
    return render(request, "tasks/create.html", context)
