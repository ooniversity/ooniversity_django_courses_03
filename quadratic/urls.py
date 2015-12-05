from django.conf.urls import patterns, url

from quadratic import views

urlpatterns = patterns('',
					   # url(r'^$', 'Norm', name='home'),
					   url(r'^results/$', views.quadratic_results, name='results'),
					   )
