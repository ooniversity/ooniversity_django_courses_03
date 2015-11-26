from django.contrib import admin
from courses.models import Course, Lesson

class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('../static/js/bootstrap.js'
              )
        css = {
               'all':('../static/css/bootstrap.css','../static/css/style.css')
               }

admin.site.register(Course)
admin.site.register(Lesson)
# Register your models here.
