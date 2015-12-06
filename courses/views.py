from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages

def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course_id = course_id)
    coach = Coach.objects.get(coach_courses = course_id)
    assistant = Coach.objects.get(assistant_courses = course_id)
    return render (request, 'courses/detail.html',{'course':course,'lessons':lessons, 'coach': coach, 'assistant':assistant})
    
def add(request):
  if request.POST:
    form = CourseModelForm(request.POST)
    if form.is_valid():
      form.save()
      text =  "Course %s has been successfully added." %(form.cleaned_data['name'])
      messages.success(request, text)
      return redirect('index')
  else:
    form = CourseModelForm()
  return render(request, 'courses/add.html', {'form': form})
    
def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    form = CourseModelForm(instance=course)
    if request.POST:
      form = CourseModelForm(request.POST, instance=course)
      if form.is_valid():
        form.save()
        text = "The changes have been saved."
        messages.success(request, text)
        return redirect('courses:edit', course_id)
    return render(request, 'courses/edit.html', {'form': form})    

def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    form = CourseModelForm(instance=course)
    if request.POST:
      text = "Course %s has been deleted." %(course.name)
      messages.success(request, text)  
      course.delete()
      return redirect('index')
    return render(request, 'courses/remove.html', {'form': form})
    
def add_lesson(request, course_id):
  if request.POST:
    form = LessonModelForm(request.POST)
    if form.is_valid():
      form.save()
      text =  "Lesson %s has been successfully added." %(form.cleaned_data['subject'])
      messages.success(request, text)
      return redirect('courses:detail', course_id)
  else:
    form = LessonModelForm()
  return render(request, 'courses/add_lesson.html', {'form': form})