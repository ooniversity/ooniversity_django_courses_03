from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'skype']

    search_fields = ['surname', 'email']

    fieldsets = [('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
                 ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
                 (None, {'fields': ['courses']})]

    filter_horizontal = ['courses']

    def fullname(self, obj):
        return obj.fullname()

    fullname.short_description = 'Full name'


admin.site.register(Student, StudentAdmin)
