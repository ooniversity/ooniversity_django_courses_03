from django.conf.urls import patterns, include, url
from students import views

urlpatterns = patterns('',
    url(r'remove/(?P<pk>\d+)/$', views.remove, name='remove'),
    url(r'edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'(?P<student_id>\d+)/$', views.student_detail, name='student_detail'),
    url(r'add/$', views.create, name='add'),

    url(r'$', views.list_view, name='list_view'),
)
