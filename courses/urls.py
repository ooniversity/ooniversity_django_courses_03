from django.conf.urls import patterns, url
import views


urlpatterns = patterns('',
        url(r'(\d{1})/$', views.detail, name='detail'),
        url(r'^add/$', views.add, name='add'),
        url(r'^edit/(?P<cours_id>\d+)/$', views.edit, name='edit'),
        url(r'^remove/(?P<cours_id>\d+)/$', views.remove, name='remove'),
        )

