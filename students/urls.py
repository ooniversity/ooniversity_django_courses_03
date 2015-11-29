from django.conf.urls import patterns, include, url
from students import views

urlpatterns = patterns('',
    url(r'^$', views.list_view, name='list_view'),
    url(r'^(?P<students_id>\d+)/$', views.detail, name='detail'),
)
