from django.conf.urls import patterns, url
#from courses.models import Course
from coaches import views

urlpatterns = patterns('',
    #url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),
	#url(r'^$', views.list_view, name='list_view'),
	url(r'(?P<detail_id>\d+)/$', views.detail, name='detail'),
  
)
