from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
	search_fields = ['surname', 'email']
	list_display = ['full_name', 'email', 'skype']

	filter_horizontal = ['courses']
	fieldsets = [
				('Personal info', {'fields' : ['name', 'surname', 'date_of_birth']}),
				('Contact info', {'fields' : ['email', 'phone', 'address', 'skype']}),
				(None, {'fields': ['courses']}),
				]
#    fieldsets = [('Personal info', {'fields': ['name', 'surname', 'birth_date']}),
##        		 ('Contact info', {'fields': ['email', 'phone', 'address', 'scype']}),      
#        		 (None, {'fields': ['courses']}),   
#    ]

	def full_name(self, obj):
		return obj.name + " " + obj.surname



admin.site.register(Student, StudentAdmin)