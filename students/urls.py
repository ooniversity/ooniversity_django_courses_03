from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',

        url(r'^$', views.StudentListView.as_view(), name='list_view'),
        url(r'^(?P<student_id>\d+)/$', views.StudentDetailView.as_view(pk_url_kwarg='student_id'), name='detail'),
        url(r'^add/$', views.StudentCreateView.as_view(), name='add'),
        url(r'^edit/(?P<student_id>\d+)/$', views.StudentUpdateView.as_view(pk_url_kwarg='student_id'), name='edit'),
        url(r'^remove/(?P<student_id>\d+)/$', views.StudentDeleteView.as_view(pk_url_kwarg='student_id'), name='remove'),
)
