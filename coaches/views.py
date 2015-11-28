from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course

def detail(request, coach_id):
    courses_coach = Course.objects.filter(coach=coach_id)
    courses_assis = Course.objects.filter(assistant=coach_id)
    my_coach = Coach.objects.get(pk=coach_id)
    return render(request, "coaches/detail.html", {'my_coach': my_coach, 'courses_coach': courses_coach, 'courses_assis': courses_assis})
