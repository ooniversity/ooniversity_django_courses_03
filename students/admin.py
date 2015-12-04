from django.contrib import admin
from django.db import models
from students.models import Student
from django.forms import widgets

class StudentsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'skype']
    fieldsets = [('Personal info', {'fields': ['name', 'surname', 'date_of_birth']}),
                 ('Contact info', {'fields': ['email', 'phone', 'address', 'skype']}),
                 (None, {'fields': ['courses']})
                 ]
    formfield_overrides = {
        models.ManyToManyField: {'widget': widgets.SelectMultiple}
    }
    list_filter = ['courses']
    search_fields = ['surname', 'email']
    filter_horizontal = ['courses']

    def full_name(self, obj):
        return "%s %s" % (obj.name, obj.surname)

admin.site.register(Student, StudentsAdmin)

# Register your models here.
