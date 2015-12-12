from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    context_object_name = 'course'
    success_url = reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context
    def form_valid(self, form):
        context = super(CourseCreateView, self).form_valid(form)
        message = u'Course %s has been successfully added.' %self.object.name
        messages.success(self.request, message)
        return context

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    context_object_name = 'course'
    def get_success_url(self):
        context= reverse_lazy('courses:edit', kwargs={'pk':self.object.pk})
        return context
    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context
    def form_valid(self, form):
        context = super(CourseUpdateView, self).form_valid(form)
        message = "The changes have been saved."
        messages.success(self.request, message)
        return context

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    context_object_name = 'course'
    success_url = reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context
    def delete(self, request, *args, **kwargs):
        context = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        message = "Course %s has been deleted." %self.object.name
        messages.success(self.request, message)
        return context
    
def add_lesson(request, id):
    
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson_new = form.save()
            message = 'Lesson %s has been successfully added.' %lesson_new.subject
            messages.success(request, message)
            return redirect("courses:detail", id)
    else:
        form = LessonModelForm(initial={'course': id})
    return render(request, "courses/add_lesson.html", {'form': form})