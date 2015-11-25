from django.contrib import admin
from courses.models import Course, Lesson

class LessonInline(admin.TabularInline):
	model = Lesson
	extra = 0
	#erbose_name_plural = "LessonInline"

class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'short_description']
	search_fields = ['name']
	inlines = [LessonInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)

