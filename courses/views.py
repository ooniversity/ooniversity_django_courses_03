# -*- coding: utf-8 -*-
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pybursa.utils import MixinLessonContext
import logging


logger = logging.getLogger(__name__) #courses.view


class CourseDetailView(DetailView):
	model = Course
	template_name = 'courses/detail.html'
	context_object_name = "course"
	
	def get_context_data(self, **kwargs):
		context = super(CourseDetailView, self).get_context_data(**kwargs)
		logger.debug("Courses detail view has been debugged")
		logger.info("Logger of courses detail view informs you!")
		logger.warning("Logger of courses detail view warns you!")
		logger.error("Courses detail view went wrong!")
		context['lessons'] = Lesson.objects.filter(course = self.object)
		return context
        
        
class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

    def form_valid(self, form):
        student = form.save()
        messages.success(self.request, u'Course %s has been successfully added.' % (student.name))
        return super(CourseCreateView, self).form_valid(form)
        
        
class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    
    def get_success_url(self):
        return reverse('courses:edit', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context
        
    def form_valid(self, form):
        student = form.save()
        messages.success(self.request, u'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context
        
    def delete(self, request, pk, *args, **kwargs):
        application = Course.objects.get(id=pk)
        messages.success(self.request, u'Course %s has been deleted.' % (application.name))
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)


class LessonCreateView(MixinLessonContext, CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'

    def get_initial(self, **kwargs):
    	#import pdb; pdb.set_trace()
        initial = {'course': self.kwargs['pk']}
        return initial
    
    def form_valid(self, form):
        lesson = form.save()
        messages.success(self.request, u'Lesson %s has been successfully added.' % lesson.subject)
        return super(LessonCreateView, self).form_valid(form)
        
        
'''	
def detail(request, pk):
	course = Course.objects.get(id = pk)
	lessons = Lesson.objects.filter(course = pk)
	return render(request, 'courses/detail.html', {'course' : course, 'lessons' : lessons})
	
	
def create(request):
	if request.method == 'POST':	
		model_form = CourseModelForm(request.POST)
		if model_form.is_valid():
			application = model_form.save()
			name = model_form.cleaned_data['name']
			messages.success(request, u'Course %s has been successfully added.' % (name))
			return redirect('index')
	else:
		model_form = CourseModelForm()
	return render(request, 'courses/add.html', {'model_form': model_form})

	
def edit(request, pk):
	application = Course.objects.get(id=pk)
	if request.method == 'POST':	
		model_form = CourseModelForm(request.POST, instance=application)
		if model_form.is_valid():
			application = model_form.save()
			messages.success(request, u'The changes have been saved.')
			return redirect('courses:edit', application.id)
	else:
		model_form = CourseModelForm(instance=application)
	return render(request, 'courses/edit.html', {'model_form': model_form})


def remove(request, pk):
	application = Course.objects.get(id=pk)
	if request.method == 'POST':
		application.delete()	
		messages.success(request, u'Course %s has been deleted.' % (application.name))
		return redirect('index')
	return render(request, 'courses/remove.html', {'application': application})

	
def add_lesson(request, pk):
	course = Course.objects.get(id=pk)
	if request.method == 'POST':	
		model_form = LessonModelForm(request.POST)
		if model_form.is_valid():	
			model_form.save()
			name = model_form.cleaned_data['subject']
			messages.success(request, u'Lesson %s has been successfully added.' % (name))
			return redirect('courses:detail', course.id)
	else:
		model_form = LessonModelForm(initial={'course': pk})
	return render(request, 'courses/add_lesson.html', {'model_form': model_form})
'''
