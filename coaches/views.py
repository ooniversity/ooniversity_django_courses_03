from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, pk):
    coaches = Coach.objects.get(id=pk)
    coach_courses = Course.objects.filter(coach=pk)
    assistant_courses = Course.objects.filter(coach=pk)
    # print assistant_courses
    return render(request, 'coaches/detail.html', {
        'coaches': coaches,
        'coach_courses': coach_courses,
        'assistant_courses': assistant_courses})
