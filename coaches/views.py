from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course

def detail(request, teacher_id):
	teacher = Coach.objects.get(id=teacher_id)
	return render(request, 'coaches/detail.html', {'teacher':teacher})
