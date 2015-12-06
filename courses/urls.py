from django.conf.urls import patterns, include, url
from courses import views

urlpatterns = patterns('',
    # course actions
    url(r'add/$', views.add, name='add'),
    url(r'remove/(?P<pk>\d+)/$', views.remove, name='remove'),
    url(r'edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    # lessons actions
    url(r'(?P<pk>\d+)/add_lesson/$', views.add_lesson, name='add_lesson'),
    # detail
    url(r'^(?P<course_id>\d+)/$', views.couse_detail, name='course_detail'),


)
