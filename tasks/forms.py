from django import forms
from django.forms import ModelForm
from tasks.models import Task


class TaskForm(ModelForm):
    class Meta:
            model = Task
            fields = ["name", "start_date", "due_date", "assignee", "notes"]
            widgets = {
                'start_date': forms.SelectDateWidget(),
                'due_date': forms.SelectDateWidget()
            }


class NotesForm(ModelForm):
    class Meta:
        model = Task
        fields = ["notes"]
