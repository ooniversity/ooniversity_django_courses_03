from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse,  reverse_lazy
from django.views import generic
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from polls.models import Choice, Question
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/detail.html"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['course_lessons'] = Lesson.objects.filter(course_id=self.object.id)
        context['course_par'] = "?course_id=" + str(self.object.id)
        return context

def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    course_lessons = Lesson.objects.filter(course_id = course_id)
    course_par = "?course_id=" + course_id
    return render(request, 'courses/detail.html', {'course_lessons': course_lessons, 'course': course, 'course_par': course_par})

class CourseCreateView(CreateView):
    model = Course
    template_name = "courses/add.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        added_course = form.save()
        success_mes = 'Course %s has been successfully added.' % (added_course)
        messages.success(self.request, success_mes, extra_tags='msg')
        return super(CourseCreateView, self).form_valid(form)

"""
def add(request):

    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            added_course = form.save()
            messages.success(request, 'Course %s has been successfully added.' % added_course)
            return redirect('/')
    else:
        form = CourseModelForm()

    return render(request, 'courses/add.html', {"form": form})
"""

def add_lesson(request, course_id):

    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form =LessonModelForm(request.POST)
        if form.is_valid():
            added_lesson = form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % added_lesson)
            return redirect('courses:detail', course_id=course.id)
    else:
        form = LessonModelForm(initial={'course': course})

    return render(request, 'courses/add_lesson.html', {"form": form})

class CourseUpdateView(UpdateView):
    model = Course
    template_name = "courses/edit.html"
    #success_url = reverse_lazy('courses:edit')

    def get_success_url(self):
        return reverse('courses:edit', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

    def form_valid(self, form):
        messages.success(self.request, 'The changes have been saved.', extra_tags='msg')
        return super(CourseUpdateView, self).form_valid(form)
"""
def edit(request, course_id):

    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', course_id = course.id)
    else:
        form = CourseModelForm(instance=course)

    return render(request, 'courses/edit.html', {'form': form})
"""
class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def get_object(self):
        deleted_course = super(CourseDeleteView, self).get_object()
        messages.success(self.request, 'Course %s has been deleted.' % deleted_course, extra_tags='msg')
        return deleted_course

def remove(request, course_id):

    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course %s has been deleted.' % course)
        return redirect('/')

    return render(request, 'courses/remove.html', {'course': course})

