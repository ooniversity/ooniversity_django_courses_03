from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import hello, hello_python, student_list, student_detail

urlpatterns = [
    url(r'^$', hello, name='home'),
    url(r'^contact/$', hello_python),
    url(r'^student_list/$', student_list),
    url(r'^student_detail/$', student_detail),
    url(r'^instructors/$', 'polls.views.instructors_list'),

    url(r'^admin/', include(admin.site.urls)),
]
