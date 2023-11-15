from django.db import models
from django.conf import settings
from projects.models import Project
from datetime import date



# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField(null = True, default = date.today)
    due_date = models.DateField(null = True, default = date.today)
    notes = models.TextField(null = True, blank = True)
    is_completed = models.BooleanField(default = False)
    project = models.ManyToManyField(
        Project,
        related_name="tasks",
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="tasks",
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name

    def get_project(self):
        return "\n".join([p.name for p in self.project.all()])
