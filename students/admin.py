from django.contrib import admin
from students.models import Student
from courses.models import Course, Lesson

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['surname', 'email']
    list_display = ('full_name', 'email', 'skype')
    list_filter = ['courses']

    fieldsets = [
        ('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
        ('Contact info',  {'fields': ['email', 'phone', 'address', 'skype']}),
    ]
    filter_horizontal = ('courses',)

    def full_name(self, obj):
        return obj.full_name()

admin.site.register(Student, StudentAdmin)
