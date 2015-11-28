from django.shortcuts import render
from students.models import Student

def list_view(request):
    r = request.GET
    if 'course_id' in r:
        students=Student.objects.filter(courses=r['course_id'])
    else:
        students=Student.objects.all()
    return render(request, 'students/list_view.html', {'students': students})


def detail(request, pk):
    return render(request, 'students/detail.html', { 'student' : Student.objects.get(id=pk)})