from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',
    url(r'^$', views.CourseListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detail'),
)