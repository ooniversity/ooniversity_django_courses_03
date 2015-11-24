from django.contrib import admin
from students.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
	list_display = ['name_surname', 'email', 'skype']
	search_fields = ['surname', 'email']
	list_filter = ['courses']
	fieldsets = [
        ('Personal info',{'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info', {'fields': ['email', 'phone', 'adress', 'skype', 'course']}),
    ]

admin.site.register(Student, StudentAdmin)
