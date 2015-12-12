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
  template_name = 'courses/detail.html'
  context_object_name = 'item'
  def get_context_data(self, **kwargs):
    context = super(CourseDetailView, self).get_context_data(**kwargs)
    context['lessons'] = Lesson.objects.filter(course_id=kwargs['object'].id)
    context['coach'] = kwargs['object'].coach
    context['assistant'] = kwargs['object'].assistant
    return context


class CourseCreateView(CreateView):
  model = Course
  template_name = 'courses/add.html'
  success_url = reverse_lazy('index')
  def form_valid(self, form):
    course = form.save()
    messages.success(self.request, "Course %s has been successfully added." % course.name)
    return super(CourseCreateView, self).form_valid(form)
  def get_context_data(self, **kwargs):
    context = super(CourseCreateView, self).get_context_data(**kwargs)
    context['title'] = u"Course creation"
    return context


class CourseUpdateView(UpdateView):
  model = Course
  template_name = 'courses/edit.html'
  success_url = reverse_lazy('index')
  def form_valid(self, form):
    course = form.save()
    messages.success(self.request, 'The changes have been saved.')
    return super(CourseUpdateView, self).form_valid(form)
  def get_context_data(self, **kwargs):
    context = super(CourseUpdateView, self).get_context_data(**kwargs)
    context['title'] = u"Course update"
    return context


class CourseDeleteView(DeleteView):
  model = Course
  template_name = 'courses/remove.html'
  success_url = reverse_lazy('index')
  def get_context_data(self, **kwargs):
    context = super(CourseDeleteView, self).get_context_data(**kwargs)
    course = kwargs['object']
    messages.success(self.request, "Course %s has been deleted." % course.name)
    context['title'] = "Course deletion"
    return context

    
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