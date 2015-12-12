# -*- coding: utf-8 -*-
from django.contrib import admin
from feedbacks.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['from_email', 'create_date']


