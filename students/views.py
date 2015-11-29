from django.shortcuts import get_object_or_404, render
from students.models import Student
from courses.models import Course

def list_view(request):
    students_course = request.GET
    if 'course_id' in students_course:
        students_on_course = Student.objects.filter(courses=students_course['course_id'])
    else:  
        students_on_course = Student.objects.all()
    return render(request, 'students/list.html', {
			      "students_on_course": students_on_course ,
			       })
def detail(request, students_id):
	students_on_course = Student.objects.filter(pk=students_id)
	return render(request, 'students/detail.html', {
                  'students_on_course': students_on_course
                  })
