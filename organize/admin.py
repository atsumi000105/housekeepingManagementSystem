from django.contrib import admin
from .models import Asset
from .models import Task
from .models import Worker
from .models import merge


admin.site.register(Asset)
admin.site.register(Task)
admin.site.register(Worker)
admin.site.register(merge)
