from django.contrib import admin
from students.models import Student
from students.models import CourseApplication


class StudentAdmin(admin.ModelAdmin):
	search_fields = ['surname', 'email']
	list_display = ['full_name',  'email', 'skype']
	list_filter = ['courses']
	
	fieldsets = [
        ('Personal info',{'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
		(None, {'fields': ['courses']}),
    ]
	filter_horizontal = [ 'courses' ]

admin.site.register(Student, StudentAdmin)
admin.site.register(CourseApplication)
