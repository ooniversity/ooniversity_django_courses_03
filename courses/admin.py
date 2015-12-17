from django.contrib import admin
from courses.models import Course, Lesson

class LessonInline(admin.TabularInline):
	model = Lesson

class CourseAdmin(admin.ModelAdmin):
	search_fields = ['name']
	inlines = [LessonInline]
	list_display = ['name', 'short_description']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)

