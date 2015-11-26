from django.shortcuts import get_object_or_404, render
from courses.models import Course, Lesson

	
def detail(request, pk):
	courses = get_object_or_404(Course, id=pk)
	return render(request, 'courses/detail.html', {'courses': courses})
