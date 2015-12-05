from django.conf.urls import patterns, include, url
from django.contrib import admin
from quadratic import views

urlpatterns = patterns('',
<<<<<<< HEAD
    url(r'^results/', views.quadratic_results, name='results'),
    #url(r'^admin/', include(admin.site.urls)),
)
=======
                       url(r"results/$", views.quadratic_results, name='results'),
                       )
>>>>>>> d1b3cd7... rewrite quadratic with form (7.2) - final commit before check
