from django.conf.urls import patterns, include, url
from students.views import detail


urlpatterns = patterns('',
    url(r'^course_id=(?P<course_id>\d)/$', detail, name='detail'),
)
