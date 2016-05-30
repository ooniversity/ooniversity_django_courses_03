from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^results/$', views.quadratic_results, name='quadratic_results')
)
