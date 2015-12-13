from django.contrib import admin
from students.models import Student
from courses.models import Course

class StudentAdmin (admin.ModelAdmin):
    filter_horizontal = ('courses',)
    list_display = ('full_name', 'email', 'skype')
    search_fields = ['surname', 'email']    
    list_filter = ['courses']
    fieldsets = [
    ('Personal info', {'fields': ['name', 'surname','date_of_birth']}),
    ('Contact info', {'fields': ['email', 'phone','address', 'skype']}),
    ('Courses',{'fields': ['courses']})
    ]
    
admin.site.register(Student, StudentAdmin)
