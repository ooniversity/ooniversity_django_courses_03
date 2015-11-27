from django.shortcuts import render
from students.models import Student
from courses.models import Course

def list_view(request):
  course_id = request.GET.get('course_id')
  if course_id != None and course_id != '':
    course = Course.objects.get(id=course_id)
    stud = Student.objects.all()
    students = []
    for man in stud:
      if course in man.courses.all():
        students.append(man)
    return render(request, 'students/list.html', {'students':students})
  else:
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students':students})

def detail(request, student_id):
  student = Student.objects.get(id=student_id)
  return render(request, 'students/detail.html', {'student':student})