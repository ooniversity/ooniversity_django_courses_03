from django.contrib import admin
from students.models import Student


    

class StudentAdmin(admin.ModelAdmin):
    list_display = ('make_full_name', 'email', 'skype')
    list_filter = ['courses']
    search_fields = ['surname', 'email']
    fieldsets = [
            ('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
            ('Contact info', {'fields': ['email', 'phone', 'address', 'skype', 'courses']}),
        ]
    filter_horizontal = ['courses']
    def make_full_name(self, Student):
        return ("%s %s" % (Student.name, Student.surname))
    make_full_name.short_description = 'Full name'



admin.site.register(Student, StudentAdmin)

