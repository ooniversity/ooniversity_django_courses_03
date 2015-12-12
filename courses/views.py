from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

def index(request):

    courses_list = Course.objects.all()

    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'courses_list': courses_list,
    })
    return HttpResponse(template.render(context))


def couse_detail(request, course_id):

    course = Course.objects.get(pk = course_id)
    lessons_list = Lesson.objects.filter(course = course)
    template = loader.get_template('courses/detail.html')
    context = RequestContext(request, {
        'course': course,
        'lessons_list': lessons_list
    })
    return HttpResponse(template.render(context))


# Add
def add(request):
    form = CourseModelForm()
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            c_name = form.data.get('name')
            messages.success(request, 'Course %s has been successfully added.'% c_name)
            return redirect('index')

    template = loader.get_template('courses/add.html')
    context = RequestContext(request, {
        'form': form
    })
    return HttpResponse(template.render(context))


# add_lesson
def add_lesson(request, pk):

    course = Course.objects.get(id=pk)
    form = LessonModelForm(initial={'course': course})
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            form.save()
            l_name = form.cleaned_data['subject']
            messages.success(request, 'Lesson %s has been successfully added.'% l_name)
            return redirect('courses:course_detail', course_id=pk)

    template = loader.get_template('courses/add_lesson.html')
    context = RequestContext(request, {
        'form': form
    })
    return HttpResponse(template.render(context))


# Delete
def remove(request, pk):
    course = Course.objects.get(id=pk)

    if request.method == 'POST':
        c_name = course.name
        course.delete()
        messages.success(request, 'Course %s has been deleted.'% c_name)
        return redirect('index')

    template = loader.get_template('courses/remove.html')
    context = RequestContext(request, {
        'course': course
    })
    return HttpResponse(template.render(context))


# Edit
def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', pk=pk)
    else:
        form = CourseModelForm(instance=course)

    template = loader.get_template('courses/edit.html')
    context = RequestContext(request, {
        'form': form
    })
    return HttpResponse(template.render(context))

class CourseDetailView(DetailView):
    model = Course
    template_name = "students/detail.html"
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['student'] = context['object']
        return context


class CourseCreateView(CreateView):
    model = Course
    template_name = "students/add.html"
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Student successfully added.')
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = "students/edit.html"
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Student successfully edited.')
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    template_name = "students/remove.html"
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Student successfully removed.')
        return super(CourseDeleteView, self).form_valid(form)