from django.shortcuts import render
from courses.models import Course
from students.models import Student

def list_view(request):
    try:
        st_list = Student.objects.filter(courses = int(request.GET['course_id']))
    except:
        st_list = Student.objects.all()
    return render(request, "students/list.html", {'st_list': st_list})

def detail(request, stud_id):
    student = Student.objects.get(id=stud_id)
    return render(request, "students/detail.html", {'student': student})
