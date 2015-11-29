from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
	filter_horizontal = ('courses',)
	fieldsets = [
        ('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
        (None,           {'fields': ['courses']}),
    ]
	list_filter = ['courses']
	search_fields = ['surname', 'email']
	list_display = ('full_name', 'email', 'skype')

admin.site.register(Student, StudentAdmin)


