from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import hello, hello_python, home, contacts, students, student_details

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^main/$', home),
	url(r'^contacts/$', contacts),
	url(r'^students/$', students), 
	url(r'^student_details/$', student_details),
	url(r'^polls/', include('polls.urls', namespace="polls")),
)

