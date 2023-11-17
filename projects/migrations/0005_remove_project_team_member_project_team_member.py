# Generated by Django 4.2.7 on 2023-11-17 14:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0004_remove_project_owner_project_owner"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="team_member",
        ),
        migrations.AddField(
            model_name="project",
            name="team_member",
            field=models.ManyToManyField(
                null=True,
                related_name="projects1",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
