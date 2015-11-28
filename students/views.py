from django.shortcuts import render
from students.models import Student
from courses.models import Course

def list_view(request):
    q = request.GET.get('course_id', None)
    if q:
        sl = Student.objects.filter(courses = Course.objects.get(id = q))
    else:
        sl = Student.objects.all()
    cl = Course.objects.all()
    return render(request,'students/list.html', {'students_list' : sl, 'courses_list' : cl})

def detail(request, student_id):
    sd = Student.objects.get(id=student_id)
    return render(request,'students/detail.html', {'student_detail': sd} )


