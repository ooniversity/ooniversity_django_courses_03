from django.shortcuts import render
from django.contrib.auth.models import User
from coaches.models import Coach

def detail(request, user_id):
    args = {}
    coach = Coach.objects.get(id=user_id)
    args['coach'] = coach
    args['coach_courses'] = coach.coach_courses.select_related('coach_courses')
    args['assistant_courses'] = coach.assistant_courses.select_related('assistant_courses')

    return render(request, 'coaches/detail.html', args)

