from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',

        url(r'^(?P<course_id>\d+)/$', views.CourseDetailView.as_view(pk_url_kwarg='course_id'), name='detail'),
        url(r'^add/$', views.CourseCreateView.as_view(), name='add'),
        url(r'^remove/(?P<course_id>\d+)/$', views.CourseDeleteView.as_view(pk_url_kwarg='course_id'), name='remove'),
        url(r'^edit/(?P<course_id>\d+)/$', views.CourseUpdateView.as_view(pk_url_kwarg='course_id'), name='edit'),
        url(r'^(?P<course_id>\d+)/add_lesson$', views.add_lesson, name='add_lesson'),

)
