import logging

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from courses.models import Course, Lesson
from pybursa.views import MixinTitle

logger = logging.getLogger(__name__)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=self.get_object().id)
        logger.debug('Courses detail view has been debugged')
        logger.info('Logger of courses detail view informs you!')
        logger.warning('Logger of courses detail view warns you!')
        logger.error('Courses detail view went wrong!')
        return context


class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/add.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        messages.success(
            self.request, 'Course %s has been successfully added.' % (data['name']))
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        messages.success(
            self.request, 'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('courses:edit', args=(self.object.pk,))


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
        message = super(CourseDeleteView, self).delete(
            request, *args, **kwargs)
        messages.success(self.request, 'Course %s has been deleted.' % (
            self.object.name))
        return message


class LessonCreateView(MixinTitle, CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'
    title = 'Create Lesson'

    def form_valid(self, form):
        data = form.cleaned_data
        messages.success(
            self.request, 'Lesson %s has been successfully added.' % (data['subject']))
        return super(LessonCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.object.get_url()