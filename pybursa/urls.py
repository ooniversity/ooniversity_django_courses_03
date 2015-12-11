from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *


admin.site.site_header = 'PyBursa Administration'

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^contact(?:s?)\b/$', contact, name='contact'),
    url(r'courses/', include('courses.urls', namespace='courses')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
    url(r'^quadratic/result(?:s?)\b/$', 'quadratic.views.quadratic_results', name='result'),
    url(r'^base/$', base, name='base'),
    url(r'^feedback/$',include('feedbacks.urls')),
)
