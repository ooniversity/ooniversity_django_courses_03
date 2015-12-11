from django.contrib import admin
from feedbacks.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = ['subject', 'create_date']
    list_filter = ['subject', 'create_date']

# Register your models here.
admin.site.register(Feedback, FeedbackAdmin)