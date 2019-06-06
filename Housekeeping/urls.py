
from django.contrib import admin
from django.conf.urls import url, include
#from django.urls import path

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('', include('organize.urls')),
]
