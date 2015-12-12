from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['my_lessons'] = Lesson.objects.filter(course=self.object.id)
        return context


class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        self.object = form.save()
        my_message = "Course {} has been successfully added.".format(self.object.name)
        messages.success(self.request, my_message)
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course

    def get_success_url(self):
        return reverse_lazy('courses:edit', args = (self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "The changes have been saved.")
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        my_message = "Course {} has been deleted.".format(self.object.name)
        messages.success(self.request, my_message)
        return HttpResponseRedirect(success_url)



def add_lesson(request, course_id):
    if request.method == 'POST':
        lesson_form = LessonModelForm(request.POST)
        if lesson_form.is_valid():
            lesson_form.save()
            lesson_form = lesson_form.cleaned_data            
            my_message = "Lesson {} has been successfully added.".format(lesson_form['subject'])
            messages.success(request, my_message)
            return redirect ('courses:detail', course_id)
    else:
        lesson_form = LessonModelForm(initial={'course': course_id})        
    return render(request, "courses/add_lesson.html", {'lesson_form': lesson_form})
