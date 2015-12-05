from django.conf.urls import patterns, include, url
from courses import views

urlpatterns = patterns('',
    url(r'^(?P<course_id>\d+)/$', views.couse_detail, name='course_detail'),
)
