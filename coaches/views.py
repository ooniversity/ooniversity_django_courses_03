from django.shortcuts import render,  get_object_or_404
from django.db import models
import models
from courses.models import Course

"""def list_view(request):
    try:
        course_id = request.GET['course_id']
        students = models.Student.objects.filter(courses__id=course_id).order_by('id')
        selection = True
    except:
        students = models.Student.objects.all()
        selection = False

    return render(request, 'course_students.html', {'students': students,
        'selection': selection})
"""

def detail(request, coach_id):
    coach = models.Coach.objects.get(id = coach_id)
    is_coach = []
    is_assistant = []
    for i in Course.objects.all():
        if i.coach == coach:
            is_coach.append(i)
        if i.assistant == coach:
            is_assistant.append(i)

    return render(request, 'coaches/detail.html', {
            "is_coach": is_coach,
            "is_assistant": is_assistant,
            "coach": coach
            })
