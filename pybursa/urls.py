from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = "index"),
    url(r'^contact/$', views.contact, name = "contact"),
    url(r'^feedback/', include('feedbacks.urls',)),#FeedbackView.as_view(), name = "feedback"),
    url(r'^student_list/$', views.student_list, name = "student_list"),
    url(r'^student_detail/$', views.student_detail, name = "student_detail"),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
)

handler404 = 'pybursa.views.error_handler404'
handler500 = 'pybursa.views.error_handler500'
