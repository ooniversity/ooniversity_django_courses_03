from django.contrib import admin
from students.models import Student
from django.db import models


class StudentAdmin(admin.ModelAdmin):
	search_fields = ['surname', 'email']
	list_display = ['full_name', 'email', 'skype']
	list_filter = [ 'courses' ]

	def full_name(self, objct):
		return '{} {}'.format(objct.name, objct.surname)

	fieldsets = [ ('Personal info', { 'fields' : [ 'name', 'surname', 'date_of_birth' ]} ),
				  ('Contact info', { 'fields' : [ 'email', 'phone', 'address' , 'skype']} ),
				  ( None, { 'fields' : [ 'courses' ]} )]

	filter_horizontal = [ 'courses' ]


admin.site.register(Student, StudentAdmin)