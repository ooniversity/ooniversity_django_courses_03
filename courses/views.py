# -*- coding: utf-8 -*- 
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pybursa.views import MixinMessage, MixinTitle
import logging  



logger = logging.getLogger(__name__)

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        data = super(CourseDetailView, self).get_context_data(**kwargs)
        lessons = Lesson.objects.filter(course=self.object).order_by('order')
        data['lessons'] = lessons
        logger.debug("Courses detail view has been debugged")
        logger.info("Logger of courses detail view informs you!")
        logger.warning("Logger of courses detail view warns you!")
        logger.error("Courses detail view went wrong!")
        return data


class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/add.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        data = super(CourseCreateView, self).get_context_data(**kwargs)
        data['title'] = 'Course creation'
        return data

    def form_valid(self, form):
		form.save()
		mess = 'Course {} has been successfully added.'.format(form.cleaned_data['name'])
		messages.success(self.request, mess)
		return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        data = super(CourseUpdateView, self).get_context_data(**kwargs)
        data['title'] = 'Course update'
        return data

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('courses:edit', None, [self.object.id])


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        data = super(CourseDeleteView, self).get_context_data(**kwargs)
        data['title'] = 'Course deletion'
        return data

    def delete(self, request, *args, **kwargs):
        data = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        mess = 'Course {} has been deleted.'.format(self.object.name)
        messages.success(self.request, mess)
        return data


class LessonCreateView(MixinMessage, MixinTitle, CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'
    context_object_name = 'lesson'
    title = 'Lesson creation'
    success_message = {'message': 'Lesson {} has been successfully added.', 'attr': 'subject'}

    def get_success_url(self):
        return self.object.get_url()

    def get_initial(self):
        return {'course': self.kwargs['pk']}



"""
def add(request):
	if request.method == 'POST':
		form = CourseModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			mess = 'Course {} has been successfully added.'.format(application.name)
			messages.success(request, mess)
			return redirect('index')
	else:
		form = CourseModelForm()
	return render(request, 'courses/add.html', {'form': form})

def add_lesson(request, pk):
	if request.method == 'POST':
		form = LessonModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			mess = 'Lesson {} has been successfully added.'.format(application.subject)
			messages.success(request, mess)
			return redirect('courses:detail', application.course.id)
	else:
		form = LessonModelForm()
	return render(request, 'courses/add_lesson.html', {'form': form})


def edit(request, pk):
	application = Course.objects.get(id=pk)
	if request.method == 'POST':
		form = CourseModelForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			messages.success(request, 'The changes have been saved.')
			return redirect('courses:edit',  application.id)
	else:
		form = CourseModelForm(instance=application)
	return render(request, 'courses/edit.html', {'form': form})

def remove(request, pk):
    application = Course.objects.get(id=pk)
    if request.method == 'POST':
		application.delete()
		mess = 'Course {} has been deleted.'.format(application.name)
		messages.success(request, mess)
		return redirect('index')
    return render(request, 'courses/remove.html', {'name': application.name})

"""
