from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
from courses.views import *
from students.views import *
from quadratic.views import *
from feedbacks.views import *

admin.site.site_header = 'My admin'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^contact/$', contact, name='contact'),
    # url(r'^student_list/$', student_list, name='student_list'),
    # url(r'^student_detail/$', student_detail, name='student_detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
    url(r'^quadratic/results/$', quadratic_results, name='quadratic_results'),
    url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
)
