from django.shortcuts import render, get_object_or_404, redirect
from students.models import Student
from courses.models import  Course, Lesson
from students.forms import StudentModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse



def list_view(request):
    try:
        course_id = request.GET['course.id']
    except:
        course_id = None
    context ={}
    print "ID=",course_id
    if course_id == None:
        context['students'] = Student.objects.all()
    else:
        p = get_object_or_404(Course, pk = course_id)
        context['students'] = Student.objects.filter(courses = course_id)
    return render(request, 'students/list.html', context)
# Create your views here.

def detail(request, student_id):
    p = get_object_or_404(Student, pk = student_id)
    context = {}
    context['student'] = Student.objects.get(id = student_id)
    context['course'] = Student.objects.get(id = student_id)
    return render(request, 'students/detail.html', context)

def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            Student = form.save()
            message = 'Student %s %s has been successfully added.' %(form['name'].value(), form['surname'].value())
            messages.success(request, message)
            return redirect('students:list_view')

    else:
        form = StudentModelForm(request.GET)
    context = {'form': form}
    return render(request, 'students/add.html', context)

def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            message = "Info on the student has been sucessfully changed."
            messages.success(request, message)
            return redirect('students:list_view')
    else:
        form = StudentModelForm(instance=student)
    context = {'form': form}
    return render(request, 'students/edit.html', context)

def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {'student':  student}
    if request.method == "POST":
        message = "Info on %s %s has been sucessfully deleted" % (student.name, student.surname)
        student.delete()
        messages.success(request, message)

        return redirect('students:list_view')

    return render(request, 'students/remove.html', context)