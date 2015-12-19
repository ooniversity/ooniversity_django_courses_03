from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course

def detail (request, coach_id):
    ccd = Coach.objects.get(id = coach_id)
    tc = Course.objects.filter(coach = coach_id)
    ac = Course.objects.filter(assistant = coach_id)
    return render (request, 'coaches/detail.html',  {'coach_detail': ccd, 'teacher_in' : tc, 'assistant_in': ac})
