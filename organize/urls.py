from django.conf.urls import url
from . import views
#from organize.views import add_asset, add_task, add_worker, display_assets, display_tasks, display_workers
from django.contrib import admin



urlpatterns = [
    #
    url(r'^$', views.base, name='base'),
    #addasset/
    url(r'^addasset/$', views.add_asset, name='add_asset'),
    #addtask
    url(r'^addtask/$', views.add_task, name='add_task'),
    #addworker
    url(r'^addworker/$', views.add_worker, name='add_worker'),
    #dipalyassets
    url(r'showassets/$', views.display_assets, name='display_assets'),
    #displaytasks
    url(r'showtasks/$', views.display_tasks, name='display_tasks'),
    #displayworkers
    url(r'^showworkers/$', views.display_workers, name='display_workers'),

    
]
