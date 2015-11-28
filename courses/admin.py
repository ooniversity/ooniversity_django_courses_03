from django.contrib import admin
#from django.forms import widgets
from courses.models import Course, Lesson

class LessonInline(admin.TabularInline):
    model = Lesson
    
class CourseAdmin(admin.ModelAdmin):
    model = Course
    search_fields = ['name']
    list_display = ['name','short_description']
    inlines = [LessonInline]
    
admin.site.register(Course, CourseAdmin)
#admin.site.register(Lesson)
