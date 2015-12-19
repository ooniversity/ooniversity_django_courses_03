import logging
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from coaches.models import Coach
from django.core.urlresolvers import reverse_lazy
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView



logger = logging.getLogger(__name__)

class CourseDetailView(DetailView):
  model = Course
  fields = '__all__'
  template_name = 'courses/detail.html'
  context_object_name = 'course'
  def get_context_data(self, **kwargs):
    logger.debug('Courses detail view has been debugged')
    logger.info('Logger of courses detail view informs you!')
    logger.warning('Logger of courses detail view warns you!')
    logger.error('Courses detail view went wrong!')
    context = super(CourseDetailView, self).get_context_data(**kwargs)
    context['lessons'] = Lesson.objects.filter(course_id=kwargs['object'].id)
    context['coach'] = kwargs['object'].coach
    context['assistant'] = kwargs['object'].assistant
    return context


class CourseCreateView(CreateView):
  model = Course
  fields = '__all__'
  template_name = 'courses/add.html'
  success_url = reverse_lazy('index')
  def form_valid(self, form):
    message_create = super(CourseCreateView, self).form_valid(form)
    messages.success(self.request, "Course %s has been successfully added." %form.cleaned_data['name'])
    return message_create
  def get_context_data(self, **kwargs):
    context = super(CourseCreateView, self).get_context_data(**kwargs)
    context['title'] = u"Course creation"
    return context


class CourseUpdateView(UpdateView):
  model = Course
  template_name = 'courses/edit.html'
  success_url = reverse_lazy('index')
  def form_valid(self, form):
    message_update = super(CourseUpdateView, self).form_valid(form)
    messages.success(self.request, "The changes have been saved.")
    return message_update
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
			form.save()
			messages.success(request, 'Lesson %s has been successfully added.' %(lesson.subject))
			return redirect('courses:detail', course_id)
	else:
		form = LessonModelForm(initial={'courses': course_id})
    
	return render(request, 'courses/add_lesson.html', {'form':form})