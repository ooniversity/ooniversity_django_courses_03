from django.conf.urls import patterns, url
from students import views


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.list_view, name='list_view'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.create, name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.remove, name='remove'),
)