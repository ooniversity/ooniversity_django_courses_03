from django.conf.urls import patterns, include, url
from django.contrib import admin

from feedbacks.views import FeedbackView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pybursa.views.index', name='index'),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
    url(r'^contact/$', 'pybursa.views.contact', name='contact'),
    url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
    url(r'^student_list/$', 'pybursa.views.student_list', name='student_list'),
    url(r'^student_detail/$', 'pybursa.views.student_detail', name='student_detail'),
	)