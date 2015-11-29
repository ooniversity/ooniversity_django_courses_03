# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Coach
from django.contrib.auth.models import User


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'skype', 'description')
    list_filter = ['user__is_staff']
