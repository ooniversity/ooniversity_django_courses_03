from django.contrib import admin
from students.models import Student
from courses.models import Course

class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'skype')
    list_filter = ['courses']
    search_fields = ['surname', 'email']
    filter_horisontal = ('courses',)

    fieldsets = (
        ('Personal info', {'fields': ('name', 'surname', 'date_of_birth')}),
        ('Contact info', {'fields': ('email', 'phon', 'address', 'skype')}),
        (None, {'fields': ('courses',)}),
    )


    def full_name(self, obj):
        return "%s %s" % (obj.name, obj.surname)
    full_name.short_description = 'full_name'


admin.site.register(Student, StudentAdmin)



