from django.conf.urls import patterns, include, url
from django.contrib import admin
from quadratic import views

urlpatterns = patterns('',
    url(r'^results/', views.quadratic_results, name='results'),
    url(r'^admin/', include(admin.site.urls)),
)
