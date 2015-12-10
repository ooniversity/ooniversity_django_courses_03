from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class CourseDetailView(DetailView):
	model = Course
	context_object_name = 'course'
	template_name = 'courses/detail.html'

	def get_context_data(self, **kwargs):
		context = super(CourseDetailView, self).get_context_data(**kwargs)
		context['lessons'] = Lesson.objects.filter(course=self.get_object().id)
		return context


class CourseCreateView(CreateView):
	model = Course
	success_url = reverse_lazy('index')
	context_object_name = 'course'
	template_name = 'courses/add.html'

	def get_context_data(self, **kwargs):
		context = super(CourseCreateView, self).get_context_data(**kwargs)
		context['title'] = "Course creation"
		return context

	def form_valid(self, form):
		self.object = form.save()
		message = 'Course %s has been successfully added.' %(self.object.name)
		messages.success(self.request, message)
		return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
	model = Course
	context_object_name = 'course'
	template_name = 'courses/edit.html'

	def get_success_url(self):
		return reverse_lazy('courses:edit', kwargs={'pk': self.object.pk})

	def get_context_data(self, **kwargs):
		context = super(CourseUpdateView, self).get_context_data(**kwargs)
		context['title'] = "Course update"
		return context

	def form_valid(self, form):
		form.save()
		message = 'The changes have been saved.'
		messages.success(self.request, message)
		return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
	model = Course
	success_url = reverse_lazy('index')
	context_object_name = 'course'
	template_name = 'courses/remove.html'

	def get_context_data(self, **kwargs):
		context = super(CourseDeleteView, self).get_context_data(**kwargs)
		context['title'] = "Course deletion"
		return context

	def delete(self, request, *args, **kwargs):
		course = self.get_object()
		message = 'Course %s has been deleted.' % (course.name)
		messages.success(self.request, message)
		return super(CourseDeleteView, self).delete(request, *args, **kwargs)


"""
def detail(request, course_id):
	course = Course.objects.get(id = course_id)
	lessons = Lesson.objects.filter(course = course_id)
	coach = course.coach.full_name()
	coach_descr = course.coach.description
	c = course.coach.id
	assistant = course.assistant.full_name()
	as_descr = course.assistant.description
	a = course.assistant.id
	return render(request, 'courses/detail.html', 
		{'course':course, 'lessons':lessons, 'coach':coach, 'assistant':assistant, 'c':c, 'coach_descr':coach_descr, 'as_descr':as_descr, 'a':a})

def add(request):
	if request.POST:
		form = CourseModelForm(request.POST)
		if form.is_valid():
			course = form.save()
			messages.success(request, 'Course %s has been successfully added.' %(course.name))
			return redirect('index')
	else:
		form = CourseModelForm()
	return render(request, 'courses/add.html', {'form':form})


def edit(request, course_id):
	course = Course.objects.get(id = course_id)
	if request.POST:
		form = CourseModelForm(request.POST, instance = course)
		if form.is_valid():
			course = form.save()
			messages.success(request, 'The changes have been saved.')
			return redirect('courses:edit', course.id)
	else:
		form = CourseModelForm(instance = course)
	return render(request, 'courses/edit.html', {'form':form})


def remove(request, course_id):
	course = Course.objects.get(id = course_id)
	if request.method == 'POST':
		messages.success(request, 'Course %s has been deleted.' % (course.name))
		course.delete()
		return redirect('index')
	return render(request, 'courses/remove.html', {'course':course})
"""

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