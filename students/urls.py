from django.conf.urls import patterns, url

from students import forms

urlpatterns = patterns('',
    # ex: /polls/
    #url(r'^$', views.index, name='index'),
    #url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    #url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^$', forms.ListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', forms.DetailView.as_view(), name='detail'),
    url(r'^add/$', forms.create),
    url(r'^edit/$', forms.edit),
)
