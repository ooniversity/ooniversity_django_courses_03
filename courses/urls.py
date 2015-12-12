from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^add/$', CourseCreateView.as_view(), name="add"),
    url(r'^edit/(?P<pk>\d+)/$', CourseUpdateView.as_view(), name="edit"),
    url(r'^remove/(?P<course_id>\d+)/$', remove, name="remove"),
    url(r'^(?P<pk>\d+)/$', CourseDetailView.as_view(), name='detail'),
    url(r'^(?P<course_id>\d+)/add_lesson/$', add_lesson, name='add-lesson'),
)
