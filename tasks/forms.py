from django import forms
from django.forms import ModelForm
from tasks.models import Task
from django.contrib.auth import get_user_model


class TaskForm(ModelForm):
    class Meta:
            model = Task
            fields = ["name", "start_date", "due_date", "assignee", "status", "notes"]
            widgets = {
                'start_date': forms.SelectDateWidget(),
                'due_date': forms.SelectDateWidget()
            }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        # Exclude superuser from the assignee choices
        superuser = get_user_model().objects.filter(is_superuser=True).first()
        if superuser:
            self.fields['assignee'].queryset = get_user_model().objects.exclude(id=superuser.id)

class NotesForm(ModelForm):
    class Meta:
        model = Task
        fields = ["notes"]
