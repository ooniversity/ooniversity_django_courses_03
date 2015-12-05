from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^(?P<stud_id>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.create, name='create'),
    url(r'^$', views.list_view, name='list_view'),
)
