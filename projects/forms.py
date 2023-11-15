from django import forms
from django.forms import ModelForm
from projects.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "start_date", "due_date"]
        widgets = {
            'start_date': forms.SelectDateWidget(),
            'due_date': forms.SelectDateWidget(),
        }
