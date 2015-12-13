from django.conf.urls import patterns, include, url
from courses import views

urlpatterns = patterns('',
    # course actions
    url(r'add/$', views.CourseCreateView.as_view(), name='add'),
    url(r'remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='remove'),
    url(r'edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='edit'),
    # lessons actions
    url(r'(?P<pk>\d+)/add_lesson/$', views.add_lesson, name='add_lesson'),
    # detail
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='course_detail'),


)
