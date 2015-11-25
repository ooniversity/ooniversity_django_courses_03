# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Student


@admin.register(Student)
class ManageAuthors(admin.ModelAdmin):
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
    ]
    filter_horizontal = ('courses',)
    ordering = ['name']
