from django.contrib import admin
from django.db import models
from feedbacks.models import Feedback
from django.forms import widgets


class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ['name', 'from_email']


# Register your models here.
admin.site.register(Feedback, FeedbacksAdmin)