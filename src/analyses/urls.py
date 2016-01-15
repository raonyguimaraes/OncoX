from django.conf.urls import url

from . import views

from analyses.views import AnalysisCreate


urlpatterns = [
    url(r'^$', views.index, name='analyses'),
    url(r'^create/$', views.create, name='analyses_create'),
    # url(r'^create/$', AnalysisCreate.as_view(), name='analyses_create'),

    url(r'^bulk_actions/$', views.bulk_actions, name='bulk_actions'),
    
    # url(r'^bulk_actions/$', views.bulk_actions, name='bulk_actions'),

]