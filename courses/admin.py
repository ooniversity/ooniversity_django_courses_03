from django.contrib import admin
<<<<<<< HEAD
from courses.models import Course, Lesson


# Register your models here.
class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    search_fields = ['name']
    inlines = [LessonInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
=======

from courses.models import Course, Lesson

class CourseAdmin(admin.ModelAdmin):
    fields = ['name', 'short_description', 'coach', 'assistant']
    list_display = ('name', 'short_description', 'description', 'coach', 'assistant')
    search_fields = ['name']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)


 

>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
