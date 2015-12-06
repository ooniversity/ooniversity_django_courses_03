from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^(?P<stud_id>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.create, name='add'),
    url(r'^edit/(?P<stud_id>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<stud_id>\d+)/$', views.remove, name='remove'),
    url(r'^$', views.list_view, name='list_view'),
)
