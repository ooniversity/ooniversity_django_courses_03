from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
                       url(r'^$', views.list_view, name="list_view"),
                       url(r'^(?P<student_id>\d+)/$',
                           views.detail, name="detail"),
                       url(r'^apply/$', views.apply_to_course,
                           name='course-application'),
                       url(r'^edit_application/(?P<pk>\d+)/$',
                           views.edit_application, name='edit-application'),
                       url(r'^delete_application/(?P<pk>\d+)/$',
                           views.delete_application, name='delete-application')
                       )
