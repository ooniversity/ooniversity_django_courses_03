from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^(?P<coach_id>\d+)/$', 'coaches.views.detail', name='detail'),
)