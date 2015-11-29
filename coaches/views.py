from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, coaches_id ): 
    coaches = Coach.objects.filter(pk = coaches_id)
    coach_course = Course.objects.filter(coach=coaches_id)
    assistant_course = Course.objects.filter(assistant=coaches_id)
    return render(request, 'coaches/detail.html', {
                  'coaches': coaches,
                  'coach_course': coach_course,  
                  'assistant_course': assistant_course
                  })

