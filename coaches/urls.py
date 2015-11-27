from django.conf.urls import patterns, url
from coaches.views import detail

urlpatterns = patterns('',

                       url(r'^(?P<user_id>\d+)/$', detail, name='detail'),



                       )
