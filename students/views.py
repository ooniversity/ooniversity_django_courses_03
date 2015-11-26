from django.shortcuts import render
from students.models import Student


def detail(request, pk):
    return render(request, 'students/detail.html', { 'student' : Student.objects.get(id=pk)})

def list_view(request):
    if 'course_id' in request.GET:
        students = Student.objects.filter(courses=request.GET['course_id'])
    else:
        students = Student.objects.all()
    return render(request, 'students/list_view.html', {'students': students})
