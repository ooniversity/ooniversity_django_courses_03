from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # kz_3_1 and tutorial
                       url(r'^polls/', include('polls.urls', namespace="polls")),
                       url(r'^admin/', include(admin.site.urls)),

                       )
