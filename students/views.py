from django.shortcuts import render, redirect
from students.forms import StudentModelForm
from django.contrib import messages
from students.models import Student


def list_view(request):
    if request.GET.get('course_id'):
        student = Student.objects.filter(courses=request.GET.get('course_id'))
    else:
        student = Student.objects.all()
    return render(request, 'students/list.html', {'students_list_course': student})


def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': student})


def create(request):
    form = StudentModelForm()
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            messages.success(request, u'Student %s %s has been successfully added.' % (new_student.name, new_student.surname))
            return redirect('students:list_view')
    return render(request, 'students/add.html', {'form': form})


def edit(request, student_id):
    our_student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST,instance=our_student)
        if form.is_valid():
            form.save()
            messages.success(request, u'Info on the student has been successfully changed.')
            return redirect('students:edit', student_id)
    else:
        form = StudentModelForm(instance=our_student)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, student_id):
    our_student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        our_student.delete()
        messages.success(request, u'Student %s %s has been successfully deleted.' % (our_student.name, our_student.surname))
        return redirect('students:list_view')
    else:
        message = '%s %s' % (our_student.name, our_student.surname)
    return render(request, 'students/remove.html', {'message': message})