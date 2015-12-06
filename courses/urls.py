from django.conf.urls import patterns, url
from courses.models import Course
from courses import views

urlpatterns = patterns('',
    url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<pk>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.remove, name='remove'),
)
