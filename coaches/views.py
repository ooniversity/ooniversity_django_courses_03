from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course

def detail (request, coach_id):
       co = Coach.objects.get(id = coach_id)
       cf = Course.objects.filter(coach = coach_id) 
       ca = Course.objects.filter(assistant = coach_id)  
       return render (request, 'coaches/detail.html',  {'coach_detail': co, 'teacher_in' : cf, 'assistant_in': ca})
