from django.conf.urls import patterns, include, url, handler404, handler500
from django.contrib import admin
from pybursa.views import index, contact, student_list, student_detail
from feedbacks import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', index, name="index"),
    url(r'^admin/', include(admin.site.urls)),
	#url(r'^$', index, name='index'),
	url(r'^contact/$', contact, name='contact'),
	url(r'^feedback/$', views.FeedbackView.as_view(), name="feedback"),
	#url(r'^student_list/$', student_list, name='student_list'), 
	#url(r'^student_detail/$', student_detail, name='student_detail'),
	url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
	
	url(r'^courses/', include('courses.urls', namespace="courses")),
	url(r'^students/', include('students.urls', namespace="students")),
	url(r'^coaches/', include('coaches.urls', namespace="coaches")),
	
)

#handler404 = 'pybursa.views.custom_page_not_found'
#handler500 = 'pybursa.views.custom_500_server_error'

