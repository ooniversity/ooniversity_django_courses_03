from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
	search_fields = ['surname', 'email']
	list_filter = ['courses']
	list_display = ['get_full_name', 'email', 'skype']
	def get_full_name(self, obj):
		return obj.name + " " + obj.surname
	get_full_name.short_description = "Full name"
	fieldsets = [('Personal info', { 'fields' : ['name', 'surname', 'date_of_birth']}), ('Contact info', {'fields' : ['email', 'phone', 'address', 'skype']}), (None, {'fields' : ['courses']})]	
	filter_horizontal = ['courses']

admin.site.register(Student, StudentAdmin)