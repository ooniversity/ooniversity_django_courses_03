from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from coaches.models import Coach
from django.core.urlresolvers import reverse_lazy
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

class CourseDetailView(DetailView):
  model = Course
  template_name = "courses/detail.html"
  context_object_name = "course"
  

class CourseCreateView(CreateView):
  form_class = CourseModelForm
  model = Course
  template_name = "courses/add.html"
  success_url = reverse_lazy("index")
  def form_valid(self, form):
    message_create = super(CourseCreateView, self).form_valid(form)
    messages.success(self.request, "Course %s has been successfully added." %form.cleaned_data['name'])
    return message_create
  def get_context_data(self, **kwargs):
    context = super(CourseCreateView,self).get_context_data(**kwargs)
    context['title'] = "Course creation"
    return context
  
class CourseUpdateView(UpdateView):
  form_class = CourseModelForm
  model = Course
  template_name = "courses/edit.html"
  def form_valid(self, form):
    message_update = super(CourseUpdateView, self).form_valid(form)
    self.success_url = reverse_lazy('courses:edit', kwargs={'pk':self.object.pk})
    messages.success(self.request, "The changes have been saved.")
    return message_update
  def get_context_data(self, **kwargs):
    context = super(CourseUpdateView, self).get_context_data(**kwargs)
    context['title'] = "Course update"
    return context
 
class CourseDeleteView(DeleteView):
  model = Course
  template_name = "courses/remove.html"
  success_url = reverse_lazy("index")
  def get_context_data(self, **kwargs):
    context = super(CourseDeleteView, self).get_context_data(**kwargs)
    context['title'] = "Course deletion"
    return context
  def delete(self, request, *args, **kwargs):
		delete_message = super(CourseDeleteView, self).delete(request, *args, **kwargs)
		messages.success(self.request, "Course %s has been deleted." % self.object.name)
		return delete_message
  
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