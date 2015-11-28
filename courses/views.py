from django.shortcuts import render
from courses.models import Course
from django.shortcuts import get_object_or_404, render


# Create your views here.
def main(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})

def detail(request, pk):
	course_object =  get_object_or_404(Course, pk=pk) 
	return render(request, 'courses/detail.html', {'course_object': course_object})
