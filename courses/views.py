from django.shortcuts import render, get_object_or_404
from courses.models import Course, Lesson
from coaches.models import Coach
from students.models import  Student
from django.core.urlresolvers import reverse


def index(request):
    context ={}
    context['courses'] = Course.objects.all()
    return render(request, 'index.html', context)

def detail (request, course_id):
    p = get_object_or_404(Course, pk = course_id)
    context ={}
    context['lessons'] = Lesson.objects.filter(course_id=course_id)
    context['course'] = Course.objects.get(id=course_id)
    context['assistant'] = Coach.objects.get(assistant_courses=course_id)
    context['coach'] = Coach.objects.get(coach_courses=course_id)
    return render(request, 'courses/detail.html', context)

# Create your views here.


