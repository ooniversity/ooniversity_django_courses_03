from django.conf.urls import patterns, url

from coaches import views



urlpatterns = patterns('',
    
    url(r'^([0-9]+)/$', views.detail, name='detail'),
)
