from django.shortcuts import get_object_or_404, render
from coaches.models import Coach
from courses.models import Course


def detail(request, pk ): 
    coaches = Coach.objects.get(id = pk)
    coach_course = Course.objects.filter(coach=pk)
    assistant_course = Course.objects.filter(assistant=pk)
    return render(request, 'coaches/detail.html', {
                  'coaches': coaches,
                  'coach_course': coach_course,  
                  'assistant_course': assistant_course
                  })


