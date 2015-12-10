from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from courses.models import Course, Lesson
from courses.forms import LessonModelForm, CourseModelForm
from django.contrib import messages


# Create your views here.
class CourseDetailView(DetailView):
    model = Course
    fields = '__all__'
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=self.get_object().id)
        return context


class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'
    context_object_name = 'course'
    template_name = 'courses/add.html'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Course creation'
        return context

    def get_success_url(self):
        message = 'Course {0} has been successfully added.'.format(self.object)
        messages.success(self.request, message)
        return reverse_lazy('index')


class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
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
    fields = '__all__'
    context_object_name = 'course'
    template_name = 'courses/remove.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['page_title'] = 'Course deletion'
        return context

    def get_success_url(self):
        message = 'Course {0} has been deleted.'.format(self.object)
        messages.success(self.request, message)
        return reverse_lazy('index')


def add_lesson(request, pk):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Lesson {0} has been successfully added.'.format(lesson.subject))
            form.save()
            messages.success(request, 'Lesson {0} has been successfully added.'.format(form.cleaned_data['subject']))
            return redirect('courses:detail', pk)
    else:
        form = LessonModelForm(initial={'course': pk})

    context = {'form': form}
    return render(request, 'courses/add_lesson.html', context)
