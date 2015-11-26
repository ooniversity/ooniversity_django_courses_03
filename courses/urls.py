from django.conf.urls import patterns, include, url
from courses import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.detail, name = 'detail'),
)
