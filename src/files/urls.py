from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list, name='files'),
    url(r'^create/$', views.create, name='files_create'),
        
]