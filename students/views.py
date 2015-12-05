from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Course, Lesson
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages

def list_view(request):
  try:
    qs = request.GET
    course = get_object_or_404(Course, pk=qs['course_id'])
    students = Student.objects.filter(courses__id = qs['course_id'])
    return render (request, 'students/list.html',{'course':course, 'students': students,})
  except:
    student_courses={}
    course = Course.objects.all()
    students = Student.objects.all()
    return render (request, 'students/list.html',{'course':course, 'students': students,})

def detail(request,student_id):
  student = get_object_or_404(Student, pk=student_id)
  courses = Course.objects.filter(student__id= student_id)
  return render (request, 'students/detail.html',{'courses':courses,'student': student})

def create(request):
  if request.POST:
    form = StudentModelForm(request.POST)
    if form.is_valid():
      form.save()
      text = "Student %s %s has been successfully added." %(form.cleaned_data['name'], form.cleaned_data['surname'])
      messages.success(request, text)
      return redirect('students:list_view')
  else:
    form = StudentModelForm()
  return render(request, 'students/add.html', {'form': form})
    
def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    form = StudentModelForm(instance=student)
    if request.POST:
      form = StudentModelForm(request.POST, instance=student)
      if form.is_valid():
        form.save()
        text = "Info on the student has been sucessfully changed."
        messages.success(request, text)
    return render(request, 'students/edit.html', {'form': form})    

def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    form = StudentModelForm(instance=student)
    if request.POST:
      text = "Info on %s %s has been sucessfully deleted." %(student.name, student.surname)
      messages.success(request, text)  
      student.delete()
      return redirect('students:list_view')
    return render(request, 'students/remove.html', {'form': form})