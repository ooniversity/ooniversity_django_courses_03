from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name = 'contact'),
    url(r'^student_list/', views.student_list, name = 'student_list'),
    url(r'^student_detail/', views.student_detail, name  = 'student_detail'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)


"""
    'http://127.0.0.1:8000/'                              =>  index                 => index                      => index.html

    'http://127.0.0.1:8000/contact/'               => contact               => contact                  => contact.html

    'http://127.0.0.1:8000/student_list/'        => student_list       => student_list           => student_list.html

    'http://127.0.0.1:8000/student_detail/'   => student_detail   => student_detail      => student_detail.html
"""