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
  def get_context_data(self, **kwargs):
    context = super(CourseDetailView,self).get_context_data(**kwargs)
    context['coach'] = Coach.objects.filter(coach_courses = self.object)
    context['assistant'] = Coach.objects.filter(assistant_courses = self.object)
    context['lessons'] = Lesson.objects.filter(course__id = self.object.id)
    return context

class CourseCreateView(CreateView):
  form_class = CourseModelForm
  model = Course
  success_url = reverse_lazy("index")
  def form_valid(self, form):
    form.save()
    messages.success(self.request, "Course %s has been successfully added." %form.cleaned_data['name'])
    return super(CourseCreateView,self).form_valid(form)
  def get_context_data(self, **kwargs):
    context = super(CourseCreateView,self).get_context_data(**kwargs)
    context['title'] = "Course creation"
    context['headline'] = "New course creation"
    return context
  
class CourseUpdateView(UpdateView):
  form_class = CourseModelForm
  model = Course
  def form_valid(self, form):
    form.save()
    self.success_url = reverse_lazy('courses:edit', kwargs={'pk':self.object.pk})
    messages.success(self.request, "The changes have been saved.")
    return super(CourseUpdateView,self).form_valid(form)
  def get_context_data(self, **kwargs):
    context = super(CourseUpdateView, self).get_context_data(**kwargs)
    context['title'] = "Course update"
    context['headline'] = "Course's data edit"
    return context
 
class CourseDeleteView(DeleteView):
  model = Course
  success_url = reverse_lazy("index")
  def get_context_data(self, **kwargs):
    context = super(CourseDeleteView, self).get_context_data(**kwargs)
    context['title'] = "Course deletion"
    messages.success(self.request, "Course %s has been deleted." % self.object.name)
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