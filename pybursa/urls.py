from django.conf.urls import patterns, include, url
from django.contrib import admin
from feedbacks.views import FeedbackView
from feedbacks import views
from pybursa import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^feedback/', FeedbackView.as_view(), name="feedback"),
    url(r'^student_list/', include('students.urls', namespace='student_list')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^student_detail/', include('students.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^quadratic/', include('quadratic.urls')),
	url(r'^courses/', include('courses.urls')),
]

handler404 = 'pybursa.views.not_found'
handler500 = 'pybursa.views.server_error'