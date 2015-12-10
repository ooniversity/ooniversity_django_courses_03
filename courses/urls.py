from django.conf.urls import patterns, url
from courses.views import CourseDeleteView, CourseDetailView, CourseCreateView, CourseUpdateView

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', CourseDetailView.as_view(), name='detail'),
    url(r'^edit/(?P<course_id>\d+)/$', CourseUpdateView.as_view, name='edit'),
    url(r'^remove/(?P<course_id>\d+)/$', CourseDeleteView.as_view, name='remove'),
    url(r'^add/$', CourseCreateView.as_view, name='add'),
    url(r'^(?P<course_id>\d+)/add_lesson$', 'courses.views.add_lesson', name='add-lesson'),
    )