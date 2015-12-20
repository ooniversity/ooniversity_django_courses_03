from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa import views
from feedbacks.views import FeedbackView

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^student_detail/$', views.student_detail, name='student_detail'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/',include('quadratic.urls')),
    url(r'courses/', include('courses.urls', namespace="courses")),
    url(r'students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    url(r'feedback/$', FeedbackView.as_view(), name='feedback'),
)

handler404 = 'pybursa.views.my_error_404'
#handler500 = 'pybursa.views.my_error_500'
