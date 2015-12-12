from django.conf.urls import patterns, url

from students import views

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
    url(r'^$', views.StudentListView.as_view(), name='list_view'),
    url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),
    #url(r'^add/$', views.create, name='add'),
    url(r'^add/$', views.StudentCreateView.as_view(), name='add'),
    #url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='edit'),
    #url(r'^remove/(?P<pk>\d+)/$', views.remove, name='remove'),
    url(r'^remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='remove'),
)
