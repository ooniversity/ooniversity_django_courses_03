from django.conf.urls import patterns, url
import views

urlpatterns = patterns('', 
	url(r'^(?P<request_id>\d+)/$', views.detail, name='detail'),
)