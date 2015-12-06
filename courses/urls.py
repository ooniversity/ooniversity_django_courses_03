from django.conf.urls import patterns, include, url
from courses.views import detail, add, edit, remove, add_lesson


urlpatterns = patterns('',
    url(r'^(?P<course_id>\d+)/$', detail, name='detail'),
    url(r'^add/$', add, name='add'),
    url(r'^edit/(?P<course_id>\d+)/$', edit, name='edit'),
    url(r'^remove/(?P<course_id>\d+)/$', remove, name='remove'),
     url(r'^add_lesson/(?P<course_id>\d+)/$', add_lesson, name='add-lesson'),
)
