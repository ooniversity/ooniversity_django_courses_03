from django.shortcuts import render, redirect
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
      course = form.save() 
      messages.success(request, "Course %s has been successfully added." %(form.cleaned_data['name']))
      return redirect('index')
  else:
    form = CourseModelForm()
  return render(request, 'courses/add.html', {'form': form})
    
def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.POST:
      form = CourseModelForm(request.POST, instance=course)
      if form.is_valid():
        course = form.save()
        messages.success(request,"The changes have been saved.")
        return redirect('courses:edit', course.id)
    else:
      form = CourseModelForm(instance = course)
    return render(request, 'courses/edit.html', {'form': form})    

def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
      messages.success(request, "Course %s has been deleted." %(course.name))  
      course.delete()
      return redirect('index')
    return render(request, 'courses/remove.html', {'course': course})
    
def add_lesson(request, course_id):
	if request.POST:
		form = LessonModelForm(request.POST)
		if form.is_valid():
			lesson = form.save()
			messages.success(request, 'Lesson %s has been successfully added.' %(lesson.subject))
			return redirect('courses:detail', course_id)
	else:
		form = LessonModelForm(initial={'course': course_id})
	return render(request, 'courses/add_lesson.html', {'form':form})