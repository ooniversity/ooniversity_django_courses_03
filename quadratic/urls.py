from django.conf.urls import patterns, url

from quadratic import views

urlpatterns = patterns('',

    url(r'^results/$', forms.quadratic_results, name = 'calculate'),

)