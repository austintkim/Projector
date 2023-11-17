from django.db import models
from django.conf import settings
from datetime import date

status_choices = (
    ("1", "Not Started"),
    ("2", "In Progress"),
    ("3", "Complete")
)


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(null = True, default = date.today)
    due_date = models.DateField(null = True, default = date.today)
    status = models.CharField(max_length=11, choices=status_choices, default='1')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="projects",
        on_delete=models.CASCADE,
        null=True
    )
    team_member = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="projects1"
    )

    def __str__(self):
        return self.name

    def get_team_member(self):
        return ", ".join([f"{user.first_name} {user.last_name}"for user in self.team_member.all()])
