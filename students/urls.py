from django.conf.urls import patterns, include, url
from students import views

urlpatterns = patterns('',
                       url(r'^$', views.list_view, name="list_view"),
                       url(r'^(?P<student_id>[1-5]{1})/$', views.detail, name="detail"),
                       url(r'^add/$', views.create, name="add"),
                       )
