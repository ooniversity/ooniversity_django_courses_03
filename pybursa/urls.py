from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^polls/', include('polls.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    #http://127.0.0.1:8000/polls/latest.html
    #url(r'^polls/latest\.html$', 'polls.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
