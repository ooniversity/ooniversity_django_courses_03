from django.shortcuts import render
from courses.models import Course
from django.shortcuts import get_object_or_404
from courses.forms import CourseModelForm, LessonModelForm
from django.shortcuts import redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course_object'


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        course = form.save()
        messages.success(self.request, "Course %s has been successfully added." % (course.name))
        return super(CourseCreateView, self).form_valid(form)

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'

    # def get_success_url(self):
    #     return reverse_lazy('courses:edit', kwargs={'pk': self.object.pk}) 

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

    def form_valid(self, form):
        messages.success(self.request, "The changes have been saved.")
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def delete(self, request, *args, **kwargs):
        message = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        success_message = "Course %s has been deleted." % (self.object.name)
        messages.success(self.request, success_message)
        return message


def add_lesson(request, pk):
    if request.method == "POST":
        form = LessonModelForm(request.POST, initial={'course': pk})
        if form.is_valid():
            lesson = form.save()
            messages.success(request, "Lesson %s has been successfully added." % (lesson.subject))
            return redirect('courses:detail', pk=pk)
    else:
        form = LessonModelForm(initial={'course': pk})
    return render(request, 'courses/add_lesson.html', {'form':form})