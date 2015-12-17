from django.shortcuts import redirect, render
from courses.models import Course, Lesson
from coaches.models import Coach
from courses import forms
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

import logging
logger = logging.getLogger(__name__)
# Create your views here.


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        logger.debug("Courses detail view has been debugged")
        logger.info("Logger of courses detail view informs you!")
        logger.warning("Logger of courses detail view warns you!")
        logger.error("Courses detail view went wrong!")
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons_list'] = Lesson.objects.filter(course_id=self.kwargs.get(self.pk_url_kwarg, None))
        context['coaches_list'] = Coach.objects.filter(coach_courses=self.kwargs.get(self.pk_url_kwarg, None))
        context['assistants_list'] = Coach.objects.filter(assistant_courses=self.kwargs.get(self.pk_url_kwarg, None))
        return context


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        course = form.cleaned_data
        messages.success(self.request, 'Course %s has been successfully added.' % course['name'])
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    context_object_name = "course"

    def get_success_url(self, **kwargs):
        return reverse_lazy('courses:edit', args=(self.object.pk,))

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

    def form_valid(self, form):
        messages.success(self.request, 'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def delete(self, request, **kwargs):
        course = self.get_object()
        message = super(CourseDeleteView, self).delete(request, **kwargs)
        messages.success(self.request, 'Course %s has been deleted.' % course.name)
        return message


def add_lesson(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % lesson.subject)
            return redirect('courses:detail', pk)
    else:
        form = forms.LessonModelForm(initial={'course': course})
    return render(request, 'courses/add_lesson.html', {'form': form})


