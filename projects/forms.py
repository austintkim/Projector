from django import forms
from django.forms import ModelForm
from projects.models import Project
from django.contrib.auth import get_user_model


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "team_member", "start_date", "due_date", "status"]
        widgets = {
            'start_date': forms.SelectDateWidget(),
            'due_date': forms.SelectDateWidget(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(ProjectForm, self).__init__(*args, **kwargs)

        # Exclude superuser from the assignee choices
        superuser = get_user_model().objects.filter(is_superuser=True).first()
        if user:
            self.fields['team_member'].queryset = get_user_model().objects.exclude(id__in=[user.id, superuser.id])
        else:
            self.fields['team_member'].queryset = get_user_model().objects.exclude(id=superuser.id)
