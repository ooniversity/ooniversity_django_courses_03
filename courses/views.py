from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Choice, Question
from courses.models import Course, Lesson

def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    course_name = course.name
    course_description = course.description
    course_lessons = Lesson.objects.filter(course_id = course_id)
    course_par = "?course_id=" + course_id
    return render(request, 'courses/detail.html', {'course_lessons': course_lessons, 'course_name':course_name, 'course_description':course_description,'course': course_par})
