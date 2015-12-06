from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('', 
	url(r'^(?P<request_id>\d+)/$', views.detail, name='detail'),
	url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<request_id>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<request_id>\d+)/$', views.remove, name='remove'),
    url(r'^(?P<request_id>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
)