from django.shortcuts import render
import models
from coaches.models import Coach
from courses.models import Course

def detail(request, pk):
    coaches = Coach.objects.get(id=pk)
    courses = Course.objects.filter(coach=pk)
    assistants = Course.objects.filter(assistant=pk)
    return render(request, 'coaches/detail.html', {
        'coaches': coaches,
        'courses': courses,
        'assistants': assistants})


    
    

