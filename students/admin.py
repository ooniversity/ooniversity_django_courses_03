# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Student


class StudentProfileInline(admin.StackedInline):
    model = Student
    filter_horizontal = ('courses',)


@admin.register(Student)
class ManageStudent(admin.ModelAdmin):
    list_display = ['name', 'surname', 'skype', 'phone']
    fieldsets = [
        (
            'Personal info:', {
                'fields': ['name', 'surname', 'date_of_birth']
            }
        ),
        (
            'Contact info:', {
                'fields': ['email', 'phone', 'address', 'skype']
            }
        ),
        (
            None, {'fields': ['courses']}
        ),
    ]
    filter_horizontal = ['courses']
    ordering = ['name']
