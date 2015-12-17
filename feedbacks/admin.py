# -*- coding: utf-8 -*-
from django.contrib import admin
from feedbacks.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('from_email', 'create_date_time')

    def create_date_time(self, obj):
        return obj.create_date.strftime("%H:%M:%S")


admin.site.register(Feedback, FeedbackAdmin)
