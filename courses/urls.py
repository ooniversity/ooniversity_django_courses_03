from django.conf.urls import patterns, include, url
from courses import views


urlpatterns = patterns('',
    url(r'^courses/$', views.courses, name='detail'),
)
