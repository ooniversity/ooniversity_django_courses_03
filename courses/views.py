from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import *
def detail(request, pk):
    
    return render(request, 'courses/detail.html', { 'course' : Course.objects.get(id=pk), 'lessons' : Lesson.objects.filter(course=pk)})
def add(request):
    #form = StudentModelForm()
    res={}   
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            data = form.cleaned_data
            messages.success(request, "Course %s has been successfully added." % course.name)
            return redirect('index')
    else:
        form = CourseModelForm() 
    res['form'] = form
    return render(request, 'students/add.html', res)
    
def edit(request, pk):
    form = CourseModelForm()
    student = Student.objects.get(id=pk)
    res={}   
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', pk)
    else:
        form = CourseModelForm(instance = student) 
    res['form'] = form
    return render(request, 'courses/edit.html', res)

def remove(request, pk):
    student = CourseModelForm(id=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Course %s has been deleted." % 
            course.name)
        return redirect('index')
    return render(request, 'courses/remove.html', {'course': course})
    
def add_lesson(request, pk):
    course = Course.objects.get(id=pk)
    res={}   
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            data = form.cleaned_data
            messages.success(request, "Lesson %s has been successfully added." % lesson.name)
            return redirect('courses:edit', pk)
    else:
        form = LessonModelForm(initial={'course': pk})
    res['form'] = form
    return render(request, 'courses/add_lesson.html', res)
        
