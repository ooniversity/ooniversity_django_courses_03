# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Student


@admin.register(Student)
class ManageAuthors(admin.ModelAdmin):
    list_display = ['name', 'surname', 'skype', 'phone']
    prepopulated_fields = {'slug': ['surname']}
    ordering = ['name']

