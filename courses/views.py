from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm


# class CourseDetailView(DetailView):
#     model = Course
#     template_name = 'courses/detail.html'
#     context_object_name = 'lessons'

#     def get_queryset(self):
#         qs = super(CourseDetailView, self).get_queryset()
#         course_id = self.request.GET.get('course_id', None)
#         if course_id:
#             qs = qs.filter(courses__id=course_id)
#         return qs
# self.kwargs['course'].pk

def detail(request, course_id):
    courses = Course.objects.get(id=course_id)
    lessons = courses.lesson_set.all()
    coaches = courses.coach.user.get_full_name()
    assistants = courses.assistant.user.get_full_name()
    return render(request,
                  'courses/detail.html', {
                      'courses': courses,
                      'lessons': lessons,
                      'coaches': coaches,
                      'assistants': assistants
                  })


def add(request):
    context = {}
    if request.POST:
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data
            form.save()
            messages.success(
                request, 'Course %s has been successfully added.' % course['name'])
            return redirect('index')
    else:
        context['form'] = CourseModelForm()
    # context['form'] = form
    return render(request, 'courses/add.html', context)


def edit(request, pk):
    context = {}
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', pk)
    else:
        context['form'] = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', context)


def remove(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        course.delete()
        messages.success(request, 'Course %s has been deleted.' % (
            course.name))
        return redirect('index')
    return render(request, 'courses/remove.html', {'course': course})


def add_lesson(request, pk):
    course = Course.objects.get(id=pk)
    if request.POST:
        form = LessonModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % (
                data['subject']))
            return redirect('courses:detail', data['course'].id)
    else:
        form = LessonModelForm(initial={'course': pk})
    return render(request, 'courses/add_lesson.html', {'form': form})
