from django.conf.urls import patterns, url

from courses.views import detail

urlpatterns = patterns('',

                       url(r'^(?P<course_id>\d+)', detail, name='detail'),



                       )
