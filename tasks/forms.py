from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        # de esta manera estilizamos formulrios desde forms.py
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a description'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

