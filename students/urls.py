from django.conf.urls import patterns, url

from students import views



urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    #url(r'^([0-9]+)/$', views.students, name='students'),
    #url(r'^(?P<course_id>\d+)$', views.students, name='students'),
    #url(r'^(?P<id_c>)$',views.students, name='students'),
    url(r'^$',views.students, name='list'),
    url(r'^([0-9]+)/$', views.list_view, name='detail'),
)
