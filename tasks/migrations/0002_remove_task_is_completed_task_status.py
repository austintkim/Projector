# Generated by Django 4.2.7 on 2023-11-16 20:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="is_completed",
        ),
        migrations.AddField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("1", "Not Started"),
                    ("2", "In Progress"),
                    ("3", "Complete"),
                ],
                default="1",
                max_length=11,
            ),
        ),
    ]
