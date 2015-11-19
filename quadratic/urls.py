from django.conf.urls import patterns, url
from quadratic import views

urlpatterns = patterns('',
	url(r'^(?P<a>\d+&<b>\d+&<c>\d+)/$', quadratic_results, name='results'),
)
