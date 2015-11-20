from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
   url(r'^results/$', views.quadratic_results, name='result')
)


