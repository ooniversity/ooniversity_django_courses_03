from django.conf.urls import url

from polls.views import *

urlpatterns = [
    # ex: /polls/
    url(r'^$', index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote'),
]