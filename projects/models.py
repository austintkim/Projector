from django.db import models
from django.conf import settings
from datetime import date


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(null = True, default = date.today)
    due_date = models.DateField(null = True, default = date.today)
    is_completed = models.BooleanField(default = False)
    owner = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="projects"
    )

    def __str__(self):
        return self.name

    def get_owner(self):
        return "\n".join([user.username for user in self.owner.all()])
