from django import forms
from organize.models import merge

class AllocateTask(forms.ModelForm):

    class Meta:
        model = merge
        fields = '__all__'