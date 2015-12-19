from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import index, contact, student_list, student_detail, IndexView
from quadratic.views import quadratic_results
from feedbacks.views import FeedbackView
from django.conf.urls import handler404, handler500



handler404 = 'pybursa.views.page_not_found'
handler500 = 'pybursa.views.server_error'






urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^contact/', contact, name='contact'),
    url(r'^feedback/', FeedbackView.as_view(), name='feedback'),
    url(r'^student_list/', student_list, name='student_list'),
    url(r'^student_detail/', student_detail, name='student_detail'),
    url(r'^quadratic/results/', quadratic_results, name='results'),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),

)