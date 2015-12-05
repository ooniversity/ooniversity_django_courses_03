from django.shortcuts import render, redirect
from courses.models import Course
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages

def list_view(request):
    course_id = request.GET.get('course_id')
    if course_id:
        course = Course.objects.get(id = course_id)
        students_list = Student.objects.all()
        students_list_course = []
        for person in students_list:
            if course in person.courses.all():
                students_list_course.append(person)
        return render(request, 'students/list.html', {'students_list_course': students_list_course})
    else:
        students_list_course = Student.objects.all()
        return render(request, 'students/list.html', {'students_list_course': students_list_course})

def detail(request, student_id):
    student = Student.objects.get(id = student_id)
    return render(request, 'students/detail.html', {'student': student})

def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            add_stud = form.save()
            messages.success(request, u'Student %s %s has been successfully added.' % (add_stud.name, add_stud.surname))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request,'students/add.html',{'form':form})

def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    message = u"%s %s" %(student.name, student.surname)
    if request.method == 'POST':
        student.delete()
        messages.success(request, u"Info on %s %s has been sucessfully deleted." % (student.name, student.surname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'message': message})

def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, u'Info on the student has been sucessfully changed.')
            return redirect('students:list_view')
    else:
        form = StudentModelForm(instance=student)
    return render(request,'students/edit.html',{'form':form})
