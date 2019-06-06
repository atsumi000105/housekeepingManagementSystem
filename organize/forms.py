from django.forms import ModelForm
from organize.models import Asset, Task, Worker

class AssetForm(ModelForm):

    class Meta:
        model = Asset
        fields = ['assetID', 'asset_name', 'volume']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields ='__all__'

class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = "__all__"
