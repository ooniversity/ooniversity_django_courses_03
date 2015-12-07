from students.forms import StudentModelForm
from django.shortcuts import render, redirect
import models


def list_view(request):
    try:
        course_id = request.GET['course_id']
        students = models.Student.objects.filter(courses__id=course_id).order_by('id')
    except:
        students = models.Student.objects.all()

    return render(request, 'students/list.html', {'students': students})


def detail(request, num):
    student = models.Student.objects.get(id = num)
    return render(request, 'students/detail.html', {'student': student})


def create(request):
    context = {}
    if request.POST: 
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    context = {'form': form}
    return render(request, 'students/add.html', context)




def remove(request):
    return render(request, 'students/remove.html')


"""
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
"""


def edit(request, stdnt_id):
    context = {}
    stdnt = Student.objects.get(id=stdnt_id)
    if request.POST:
        form = StudentModelForm(request.POST, instance=stdnt)
        if form.is_valid():
            form.save()
    else:
        form = StudentModelForm(instance=stdnt)
    
    context = {'form': form}
    return render(request, 'students/edit.html', context)



