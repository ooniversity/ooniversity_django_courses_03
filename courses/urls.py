from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<request_id>\d+)/$', views.detail, name='detail'),
)

