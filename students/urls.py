from django.conf.urls import patterns, include, url
from students import views

urlpatterns = patterns('',
                       # url(r'^$', views.list_view, name="list_view"),
                       url(r'^\d*$', views.StudentListView.as_view(), name="list_view"),
                       # url(r'^(?P<student_id>\d+)/$', views.detail, name="detail"),
                       url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name="detail"),
                       # url(r'^add/$', views.create, name="add"),
                       url(r'^add/$', views.StudentCreateView.as_view(), name="add"),
                       url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name="edit"),
                       url(r'^remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name="remove"),
                       )
