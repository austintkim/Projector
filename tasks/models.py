from django.db import models
from django.conf import settings
from projects.models import Project
from datetime import date

status_choices = (
    ("1", "Not Started"),
    ("2", "In Progress"),
    ("3", "Complete")
)



# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField(null = True, default = date.today)
    due_date = models.DateField(null = True, default = date.today)
    notes = models.TextField(null = True, blank = True)
    status = models.CharField(max_length=11, choices=status_choices, default='1')
    project = models.ForeignKey(
        Project,
        related_name="tasks",
        on_delete=models.CASCADE,
        null=True
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="tasks",
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name
