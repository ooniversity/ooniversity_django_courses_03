from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, pk):
    coaches = Coach.objects.get(id=pk)
    coach_courses = Course.objects.filter(coach=pk)
    assistants = Course.objects.filter(assistant=pk)
    # assistant_courses = Course.objects.filter(assistant=pk)
    # print assistant_courses
    return render(request, 'coaches/detail.html', {
        'coaches': coaches,
        'coach_courses': coach_courses,
        'assistants': assistants})
