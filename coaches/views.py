from django.shortcuts import render, get_object_or_404
from coaches.models import Coach


# Create your views here.
def detail(request, coach_id):
    p = get_object_or_404(Coach, pk=coach_id)
    context = {}
    context['coach'] = Coach.objects.get(id=coach_id)
    context['course_coach'] = context['coach'].coach_courses.all()
    context['course_assistant'] = context['coach'].assistant_courses.all()
    return render(request, 'coaches/detail.html', context)