from django.conf.urls import include, url, patterns
from django.contrib import admin
from .views import index, contact
from feedbacks.views import FeedbackView

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),

                       url(r'^contact/$', contact, name='contact'),

                       url(r'^feedback/$',
                           FeedbackView.as_view(), name='feedback'),

                       url(r'^quadratic/',
                           include('quadratic.urls'), name='quadratic'),

                       url(r'^polls/',
                           include('polls.urls', namespace="polls")),

                       url(r'^courses/',
                           include('courses.urls', namespace="courses")),

                       url(r'^students/',
                           include('students.urls', namespace="students")),

                       url(r'^coaches/',
                           include('coaches.urls', namespace="coaches")),

                       url(r'^admin/', include(admin.site.urls)),
                       )
