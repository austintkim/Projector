# Generated by Django 4.2.7 on 2023-11-16 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_remove_project_is_completed_project_status"),
        ("tasks", "0002_remove_task_is_completed_task_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="project",
        ),
        migrations.AddField(
            model_name="task",
            name="project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="projects.project",
            ),
        ),
    ]
