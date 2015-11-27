from django.conf.urls import patterns, url

from courses import views



urlpatterns = patterns('',
    
    url(r'^([0-9]+)/$', views.courses, name='detail'),
    
   
)
