from django.shortcuts import render
from students.models import Student
from django.shortcuts import get_object_or_404, render
from courses.models import Course


# Create your views here.
def list_view(request):
    try:
        a = request.GET.get('course_id')
        a = int(a)
        students_list = Student.objects.filter(courses=a)
    except:
        students_list = Student.objects.all()
    return render(request, 'students/list.html', {'students_list': students_list})

def detail(request, pk):
    student_object =  get_object_or_404(Student, pk=pk) 
    return render(request, 'students/detail.html', {'student_object': student_object})

def create(request):
	return render(request, 'students/add.html')