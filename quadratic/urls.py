from django.conf.urls import patterns, include, url
from django.contrib import admin

from quadratic.views import quadratic_results

urlpatterns = patterns('',

    url(r'results/', quadratic_results, name='results'),

)
