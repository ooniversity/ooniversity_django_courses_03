from django.conf.urls import patterns, url, include
from . import views
from django.contrib import admin


admin.site.site_header = 'PyBursa'

'''
urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    '',
    # ex: /cources/
    url(r'^$', views.index, name='index'),
    # ex: /cources/5/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /cources/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /cources/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)
'''

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name="index"),
    url(r'contact/', views.contact, name="contact"),
    url(r'students/', include('students.urls', namespace="students")),
    url(r'courses/', include('courses.urls', namespace="courses")),
)

