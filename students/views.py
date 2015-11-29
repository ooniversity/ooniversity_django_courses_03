from django.shortcuts import render
from students.models import Student
from courses.models import Course
def students_list(request):
    if request.GET:
        get = request.GET
        courses_list = get['course_id']
        students = Student.objects.all()
    else:
        courses_list = 'NO'
        students = Student.objects.all()

    return render(request, 'student_list.html', {'students': students, 'student_courses': Course.objects.all(),
                                                 'courses_list': courses_list})
# Create your views he