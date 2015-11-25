# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Course, Lesson


@admin.register(Course)
class ManageAuthors(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ['name']}
    ordering = ['name']


@admin.register(Lesson)
class ManageAuthors(admin.ModelAdmin):
    list_display = ['subject', 'course']
    prepopulated_fields = {'slug': ['subject']}
    ordering = ['order']
