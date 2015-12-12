from django.shortcuts import render, redirect
from courses.models import *
from courses.forms import *
from django.views.generic.edit import *
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView




# Create your views here.

class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=self.object.pk)
        context['coach'] = self.object.coach.full_name()
        context['assistant'] = self.object.assistant.full_name()
        context['coach_id'] = self.object.coach.id
        context['assistant_id'] = self.object.assistant.id
        context['coach_desc'] = self.object.coach.description
        context['assistant_desc'] = self.object.assistant.description
        context['page_title'] = '%s course detail' % (self.object)
        return context


class CourseCreateView(CreateView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/add.html'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Course creation'
        return context

    def get_success_url(self):
        message = 'Course %s has been successfully added.' % (self.object)
        messages.success(self.request, message)
        return reverse_lazy('index')


class CourseUpdateView(UpdateView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/edit.html'
    form_class = CourseModelForm

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Course update'
        return context

    def get_success_url(self):
        message = 'The changes have been saved.'
        messages.success(self.request, message)
        return reverse_lazy('courses:edit', kwargs={'pk': self.object.pk})


class CourseDeleteView(DeleteView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/remove.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['page_title'] = 'Course deletion'
        return context

    def get_success_url(self):
        message = 'Course %s has been deleted.'% (self.object)
        messages.success(self.request, message)
        return reverse_lazy('index')


def add_lesson(request, pk):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson_add = form.save()
            messages.success(request,
                    'Lesson %s has been successfully added.'% (lesson_add.subject))
            return redirect('courses:detail', pk)
    else:
        form = LessonModelForm(initial={'course': pk})

    data = {'form': form}
    return render(request, os.path.join('courses', 'add_lesson.html'), data)
