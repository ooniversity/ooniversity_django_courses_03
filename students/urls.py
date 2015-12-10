from django.conf.urls import patterns, include, url
from students import views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 


urlpatterns = patterns('',
  url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name="detail"),
  url(r'^$', views.StudentListView.as_view(), name="list_view"),
  url(r'^add/$', views.StudentCreateView.as_view(), name='add'),
  url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='edit'),
  url(r'^remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='remove'),
  
)