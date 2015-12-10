# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin 
from django.core.urlresolvers import reverse_lazy


class MixinCourseContext(object):
    
    def get_lessons(self):
        #cont = super(MixinCourseContext, self).get_context_data(**kwargs)
        lessons = Lesson.objects.filter(course_id=self.object.id)
        #Lesson.objects.filter(course__id=self.object.id)
        #course = lesson.course_id
        return lessons

    #def get_coaches(self):
        #coaches =  Coach.objects.filter(coach_courses__id=self.object.id).name   
        #return coaches

    def get_context_data(self, *args, **kwargs):
        context = super(MixinCourseContext, self).get_context_data(**kwargs)
        #context['title'] = 'Student registration'
        #self.object = self.get_object()
        context['lessons'] = self.get_lessons()
        #context['coach_name'] = self.get_coaches()
        return context
    #def dispatch(self, *args, **kwargs):
        #return super(MixinCourseContext, self).dispatch(*args, **kwargs)    
        #return super(MixinCourseContext, self).get_context_data(**kwargs)

class CourseDetailView(MixinCourseContext, DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    
    def get_context_data(self, **kwargs):
        data = super(CourseDetailView, self).get_context_data(**kwargs)
        #context['title'] = 'Student registration'
        #self.object = self.get_object()
        #print self.object
        #context['name'] = self.object.name
        #context['description'] = self.object.description
        #context['lesson1'] = Lesson.objects.filter(course__id=self.object.id)
        #context['course_id'] = self.object.id
        #args['xuy'] = 'http://127.0.0.1:8000/students/?course_id={}'.format(course_id)
        #context['coach_name'] = self.object.coach.name
        #context['coach_surname'] = self.object.coach.surname
        #context['coach_description'] = self.object.coach.description
        #context['assistant_name'] = self.object.assistant.name
        #context['assistant_surname'] = self.object.assistant.surname
        #context['assistant_description'] = self.object.assistant.description
        data['coach'] = self.object.coach
        data['assistant'] = self.object.assistant
    
        return data
        
        


def detail(request, course_id):
    #return HttpResponse('course_id = {}'.format(course_id))
    args = {}
    #args['id'] = course_id        
    course = Course.objects.get(id=course_id)
    args['name'] = course.name
    args['description'] = course.description
    args['lesson1'] = Lesson.objects.filter(course__id=course_id)
    args['course_id'] = course_id
    #args['xuy'] = 'http://127.0.0.1:8000/students/?course_id={}'.format(course_id)
    args['coach_name'] = course.coach.name
    args['coach_surname'] = course.coach.surname
    args['coach_description'] = course.coach.description
    args['assistant_name'] = course.assistant.name
    args['assistant_surname'] = course.assistant.surname
    args['assistant_description'] = course.assistant.description
    args['coach'] = course.coach
    args['assistant'] = course.assistant


    #course.coach.coach_courses.select_related('coach_courses') - курсы тренера


    return render(request, 'courses/detail.html', args)


class CourseCreateView(CreateView):
    model = Course
    #form_class = StudentModelForm
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')
    #context_object_name = 'a'

    
    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context
    def form_valid(self, form):
        course = form.save()
        messages.success(self.request, 'Course %s has been successfully added.' % (course.name))
        return super(CourseCreateView, self).form_valid(form)


def add(request):
    args = {}
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid:
            form.save()
            data = form.cleaned_data
            name = data['name']
            messages.success(request, 'Course %s has been successfully added.' % (name))
            return redirect('index')
        else:
            form = CourseModelForm(request.POST)
            args['form'] = form
            return render(request, 'courses/add.html', args)
    else:
        form = CourseModelForm()
        args['form'] = form
        return render(request, 'courses/add.html', args)


class CourseUpdateView(UpdateView):
    form_class = CourseModelForm
    model = Course
    template_name = 'courses/edit.html'
    #success_url = reverse_lazy('students:edit', get_object().id)
    def get_success_url(self):
        #if self.request.GET.get('pk'):
        #return reverse_lazy('students:edit', args=(self.request.GET.get('pk'), ))
        return reverse_lazy('courses:edit', args=(self.get_object().id, ))
    
    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context
    
    def form_valid(self, form):
        course = form.save()
        messages.success(self.request, 'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)    

def edit(request, course_id):
    args = {}
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect ('courses:edit', course_id=course_id)
        else:
            form = StudentModelForm(request.POST, instance=course)
            args['form'] = form
            return render(request, 'students/add.html', args)
    else:
        form = CourseModelForm(instance=course)
        args['form'] = form
        return render(request, 'courses/edit.html', args)

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')
    #success_message = "Thing %s was deleted successfully." 
     
    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context
    
    

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.name
        
        messages.success(request, 'Course %s has been deleted.' % (name))
        self.object.delete()
        return redirect(self.get_success_url())

def remove(request, course_id):
    args = {}
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course %s has been deleted.' % (course.name))
        return redirect ('index')
    else:
        args['course'] = course
        return render(request, 'courses/remove.html', args)


class Add_lessonCreateView(CreateView):
    model = Lesson
    form_class = LessonModelForm
    template_name = 'courses/add_lesson.html'
    #print pk
    #initial = {'course':Course.objects.get(id=course)}
    
    
    
    
    
    def form_valid(self, form):
        #data = form.cleaned_data
        lesson = form.save()
        messages.success(self.request, 'Lesson %s has been successfully added.' % (lesson.subject))
        return super(Add_lessonCreateView, self).form_valid(form)
    
    #def get_form_kwargs(self):
        #kwargs = super(Add_lessonCreateView, self).get_form_kwargs()
        #kwargs['course'] = Course.objects.get(id=3)

        #return kwargs
    
    
    #def get_form_kwargs(self):
   
        #kwargs = super(ModelFormMixin, self).get_form_kwargs()
        #if hasattr(self, 'object'):
            #kwargs.update({'instance': self.object})
        #return kwargs
    
    def get_initial(self):
        
        initial = super(Add_lessonCreateView, self).get_initial()
        initial = initial.copy()
        #self.object = self.get_object()
        #print self.object.pk
        
        #print dir(self.request.META)
        #print self.request.META['PATH_INFO']
        path = self.request.META['PATH_INFO']
        #print path
        path2 = path.strip('/courses//add_lesson')
        #print path2
        #print path
        #print dir(self.object)
        #print type(self.object)
        #print self.request
        #course = Course.objects.get(id=self.request.GET.get('course_id'))
        #lesson = Lesson.objects.all().filter(course_=path2)
        #lesson2 = Lesson.objects.get(id=path2)
        #print lesson2.
        #print lesson.get(pk=self.object.pk)
        #lesson = get_form_kwargs(self, 'instance')
        #lesson = context['lesson']
        #initial['course'] = Course.objects.get(pk=path2)
        initial['course'] = Course.objects.get(id=path2)
        
        #return { 'course': Course.objects.get(pk=path2) }
        return initial    


def add_lesson(request, pk):
    args = {}
    course = Course.objects.get(id=pk)
    #lesson = Lesson.objects.get(course = course_id)
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            
            messages.success(request, 'Lesson %s has been successfully added.' % (data['subject']))
            return redirect ('courses:detail', course_id=course_id)
        else:
            #form = StudentModelForm(request.POST)
            args['form'] = form
            return render(request, 'students/add.html', args)
    else:
        form = LessonModelForm(initial={'course': course})
        args['form'] = form
        return render(request, 'courses/add_lesson.html', args)        

