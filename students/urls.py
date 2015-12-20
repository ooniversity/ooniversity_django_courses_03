from django.conf.urls import patterns, include, url
from students import views


urlpatterns = patterns('',
    url(r'remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='remove'),
    url(r'edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='edit'),
    url(r'(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='student_detail'),
    url(r'add/$', views.StudentCreateView.as_view(), name='add'),

    url(r'$', views.StudentListView.as_view(), name='list_view'),
)

