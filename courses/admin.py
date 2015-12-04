from django.contrib import admin
from courses.models import Course, Lesson

# Register your models here.
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0
    list_display = (('subject', 'description', 'order'), )



class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description']
    inlines = [LessonInline]
    search_fields = ['name']

admin.site.register(Course, CoursesAdmin)
admin.site.register(Lesson)
