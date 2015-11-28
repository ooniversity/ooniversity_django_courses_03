from django.conf.urls import patterns, url
from students import views

urlpatterns = patterns('',
    url(r'^$', views.list_view, name='list_view'),
    url(r'(?P<detail_id>\d+)/$', views.detail, name='detail'),
)
