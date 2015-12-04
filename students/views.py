from django.shortcuts import render, redirect
from students.models import *
from students.forms import *
from courses.models import *
from django.contrib import messages

def list_view(request):
    r = request.GET
    if 'course_id' in r:
        students=Student.objects.filter(courses=r['course_id'])
    else:
        students=Student.objects.all()
    return render(request, 'students/list.html', {'students': students})


def detail(request, pk):
    return render(request, 'students/detail.html', { 'student' : Student.objects.get(id=pk)})

def create(request):
    context = {}
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            messages.success(request, 'Student %s %s has been successfully added.' % (data['name'], data['surname']))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form' : form })

def edit(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Info on the student has been sucessfully changed.')
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/edit.html', {'form': form})

def remove(request, student_id):
    student = Student.objects.get(id = student_id)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Info on %s %s has been sucessfully deleted." % (student.name, student.surname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html', { 'student' : student })