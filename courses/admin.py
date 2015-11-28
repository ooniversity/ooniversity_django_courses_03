from django.contrib import admin
from courses.models import Course, Lesson

class LessonInLine(admin.TabularInline):
    model = Lesson
    extra = 3

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    search_fields = ['name']
    inlines = [LessonInLine]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
