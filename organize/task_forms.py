from django import forms
from organize.models import Task

class AddTask(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'