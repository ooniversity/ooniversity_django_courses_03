from django.conf.urls import include, patterns, url
from polls import views
from django.contrib import admin


urlpatterns = patterns('',

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
