# -*- coding: utf-8 -*-
from courses.models import Course, Lesson
from coaches.models import Coach


class MixinCoachContext(object):
    def get_context_data(self, **kwargs):
        context = super(MixinCoachContext, self).get_context_data(**kwargs)
        context['coach_course'] = Course.objects.filter(coach=self.object)
        context['assistant_course'] = Course.objects.filter(assistant=self.object)
        return context


class MixinLessonContext(object):
    def get_context_data(self, **kwargs):
        context = super(MixinLessonContext, self).get_context_data(**kwargs)
        context['title'] = 'Создание нового занятия'
        return context
