from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from coaches.models import Coach
from django.core.urlresolvers import reverse_lazy
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class CourseDetailView(DetailView):
  template_name = "courses/detail.html"
  model = Course

class CourseCreateView(CreateView):
  template_name = "courses/add.html"
  model = Course
  success_url = reverse_lazy("index")
  
class CourseUpdateView(UpdateView):
  template_name = "courses/edit.html"
  model = Course
  success_url = reverse_lazy("index")
 
class CourseDeleteView(DeleteView):
  template_name = "courses/remove.html"
  model = Course
  success_url = reverse_lazy("index")

  

def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course_id = course_id)
    coach = Coach.objects.get(coach_courses = course_id)
    assistant = Coach.objects.get(assistant_courses = course_id)
    return render (request, 'courses/detail.html',{'course':course,'lessons':lessons, 'coach': coach, 'assistant':assistant})
    

    



    
def add_lesson(request, course_id):
	if request.method == 'POST':
		form = LessonModelForm(request.POST)
		if form.is_valid():
			lesson = form.save()
			messages.success(request, 'Lesson %s has been successfully added.' %(lesson.subject))
			return redirect('courses:detail', course_id)
	else:
		form = LessonModelForm(initial={'course': course_id})
	return render(request, 'courses/add_lesson.html', {'form':form})