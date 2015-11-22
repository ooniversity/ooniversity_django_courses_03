from django.conf.urls import patterns, url
import views
from django.http import HttpResponse

urlpatterns = patterns('',
	#url(r'^$', 'Norm', name='home'),
	url(r'^results/$', views.quadratic_results, name='results'),
)
