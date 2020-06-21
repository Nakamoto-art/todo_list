from django import forms

import datetime

from .models import Task


class TaskForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    text = forms.CharField(
                widget=forms.Textarea(
                    attrs={
                        "placeholder": "Your TODO",
                        "class": "new-class-name text",
                        "id": "my-id-for-textarea",
                        "rows": 5,
                        "cols": 50,
                    }
                )
            )
    date  = forms.DateField(initial=datetime.date.today)