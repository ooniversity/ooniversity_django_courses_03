from django.contrib import admin
from polls.models import Choice, Question

<<<<<<< HEAD
# Register your models here.

=======
>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
<<<<<<< HEAD
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
#class ChoiceInline(admin.TabularInline):
    inlines = [ChoiceInline]
=======
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172


admin.site.register(Question, QuestionAdmin)

<<<<<<< HEAD
admin.site.register(Choice)
=======
>>>>>>> ce4a1093bf62f0859191a8228e634658f2a4a172
