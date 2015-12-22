from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *
from feedbacks.views import *

admin.site.site_header = 'ITBursa'
handler404 = 'pybursa.views.my_handler404'
handler500 = 'pybursa.views.my_handler500'

urlpatterns = patterns('',

                       url(r'^$', index, name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^polls/', include('polls.urls', namespace="polls")),
                       url(r'^quadratic/result(?:s?)\b/$', 'quadratic.views.quadratic_results', name='result'),
                       url(r'^contact/$', contact, name='contact'),
                       url(r'^student_list/$', student_list, name='student_list'),
                       url(r'^student_detail/$', student_detail, name='student_detail'),
                       url(r'^courses/', include('courses.urls', namespace='courses')),
                       url(r'^students/', include('students.urls', namespace='students')),
                       url(r'^coaches/', include('coaches.urls', namespace='coaches')),
                       url(r'^feedback/', FeedbackView.as_view(), name='feedback'),

                       )
