from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from coaches.models import Coach
from forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
import logging


def detail(request, num):
    item = Course.objects.get(id=num)
    lesson = Lesson.objects.filter(course=Course.objects.filter(id=num))
    coaches = Coach.objects.filter(coach_courses=num)
    assistants = Coach.objects.filter(assistant_courses=num)
    return render(request, 'courses\detail.html', {'item': item, 'lesson': lesson,
                                                   'coaches': coaches, 'assistants': assistants
                                                   })


def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            text = "Course %s has been successfully added." % course.name
            messages.success(request, text)
            return redirect('index')

    form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})


def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            text = 'The changes have been saved.'
            messages.success(request, text)
            return redirect('courses:edit', pk)

    form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        course.delete()
        text = "Course %s has been deleted." % course.name
        messages.success(request, text)
        return redirect('index')
    return render(request, 'courses/remove.html', {'course': course})


def add_lesson(request, pk):
    form = LessonModelForm(initial={'course': pk})
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            text = "Lesson %s has been successfully added." % lesson.subject
            messages.success(request, text)
            return redirect('courses:detail', pk)
    return render(request, 'courses/add_lesson.html', {'form': form})


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        logger = logging.getLogger(__name__)
        logger.debug("Courses detail view has been debugged")
        logger.info("Logger of courses detail view informs you!")
        logger.warning("Logger of courses detail view warns you!")
        logger.error("Courses detail view went wrong!")

        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course_id=kwargs['object'].id)
        context['coach'] = kwargs['object'].coach
        context['assistant'] = kwargs['object'].assistant
        return context


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        course = form.save()
        messages.success(self.request, "Course %s has been successfully added." % course.name)
        return super(CourseCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Course creation"
        return context


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        course = form.save()
        messages.success(self.request, 'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Course update"
        return context


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        course = kwargs['object']
        messages.success(self.request, "Course %s has been deleted." % course.name)
        context['title'] = "Course deletion"
        return context









