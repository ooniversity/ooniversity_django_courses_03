from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages



def detail(request,pk):
    coach={}
    assistant={}
    course=Course.objects.get(id=pk)
    coach['fio']=course.coach.user.get_full_name()
    assistant['fio']=course.assistant.user.get_full_name()
    coach['id']=course.coach.id
    assistant['id']=course.assistant.id
    coach['description']=course.coach.description
    assistant['description']=course.assistant.description
    lessons=Lesson.objects.filter(course_id=pk)
    return render(request, 'courses/detail.html', {"lessons": lessons,"course":course,'coach':coach,'assistant':assistant})

def add(request):
    form = CourseModelForm()
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            add_course = form.save()
            messages.success(request, u'Course %s has been successfully added.' % (add_course.name))
            return redirect('index')
    return render(request,'courses/add.html',{'form':form})

def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, u'The changes have been saved.')
            return redirect('courses:edit', pk)
    else:
        form = CourseModelForm(instance=course)
    return render(request,'courses/edit.html',{'form':form})

def remove(request,pk):
    course = Course.objects.get(id=pk)
    message = u"%s" %(course.name)
    if request.method == 'POST':
        course.delete()
        messages.success(request, u"Course %s has been deleted." % (course.name))
        return redirect('index')
    return render(request, 'courses/remove.html', {'message': message})
    
def add_lesson(request,pk):  
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            add_lesson = form.save();
            messages.success(request, u"Lesson %s has been successfully added." % (add_lesson.subject))
            return redirect('courses:detail',pk)
    else:
        form = LessonModelForm(initial= {'course': pk})
    return render(request,'courses/add_lesson.html',{'form':form})