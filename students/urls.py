from django.conf.urls import patterns, url
from students import views
urlpatterns = patterns('',
    url(r'^$', views.students, name='list_view'),
    url(r'^(?P<student_id>\d+)/$', views.students_detail, name='detail'),    
)