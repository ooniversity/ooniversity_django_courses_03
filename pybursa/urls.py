from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^$', index, name='index'),
    # url(r'^contacts/$', contact),
    url(r'^contact(?:s?)\b/$', contact, name='contact'),
    url(r'^student(?:s?)_list/$', student_list, name='student_list'),
    url(r'^student_detail/$', student_detail, name='student_detail'),
    #
    # url(r'^result(?:s?)\b/$', quadratic_results, name='result'),
    # url(r'^equation/$', equation, name='equation'),
    url(r'^quadratic/$', 'quadratic.views.equation', name='equation'),
    url(r'^quadratic/result(?:s?)\b/$', 'quadratic.views.quadratic_calc', name='result'),
)
