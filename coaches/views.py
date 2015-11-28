from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course

def detail(request, coach_id):
    coach = Coach.objects.get(id = coach_id)
    courses_coach = Course.objects.filter(coach_id = coach_id)
    courses_assistant = Course.objects.filter(assistant_id = coach_id)
    course_par = "?course_id="
    return render(request, 'coaches/detail.html', {'coach': coach, 'courses_coach': courses_coach, 'courses_assistant': courses_assistant, 'course_par': course_par})
