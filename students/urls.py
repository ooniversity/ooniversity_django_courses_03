from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    #url(r'^(?P<pk>\d+)/$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.IndexView.as_view(), name='student_list'),
)
