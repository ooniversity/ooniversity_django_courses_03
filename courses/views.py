from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


def index(request):
    context ={}
    context['courses'] = Course.objects.all()
    return render(request, 'index.html', context)

'''
def detail(request, course_id):
    p = get_object_or_404(Course, pk = course_id)
    context ={}
    context['lessons'] = Lesson.objects.filter(course_id=course_id)
    context['course'] = Course.objects.get(id=course_id)
    context['assistant'] = Coach.objects.get(assistant_courses=course_id)
    context['coach'] = Coach.objects.get(coach_courses=course_id)
    return render(request, 'courses/detail.html', context)
'''

class CourseDetailView(DetailView):

    model = Course
    template_name = "courses/detail.html"
    context_object_name = "course"


class CourseCreateView(CreateView):

    model = Course
    template_name = "courses/add.html"
    success_url = reverse_lazy('index')


    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        self.object = form.save()
        message = 'Course %s has been successfully added.' %(form['name'].value())
        messages.success(self.request, message)
        return super(CourseCreateView, self).form_valid(form)


'''
def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data
            course_add = form.save()
            message = 'Course %s has been successfully added.'  % course_add.name
            messages.success(request, message)
            return redirect('index')
    else:
        form = CourseModelForm()
    context = {'form': form}
    return render(request, 'courses/add.html', context)
# Create your views here.
'''

class CourseUpdateView(UpdateView):

    model = Course
    template_name = "courses/edit.html"
    context_object_name = "course"
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

    def get_success_url(self):
        return reverse_lazy('courses:edit', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        message = super(CourseUpdateView, self).form_valid(form)
        mess = 'Course %s has been successfully updated.' %(form['name'].value())
        messages.success(self.request, mess)
        return message

'''
def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            message = "The changes have been saved."
            messages.success(request, message)
            return redirect('courses:edit', course.id)
    else:
        form = CourseModelForm(instance=course)
    context = {'form': form}
    return render(request, 'courses/edit.html', context)
'''



class CourseDeleteView(DeleteView):

    model = Course
    template_name = "courses/remove.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def delete(self, request, *args, **kwargs):
        message = super(CourseDeleteView, self).delete(request, *args, **kwargs)
        message_to_send = 'Course %s has been deleted' % self.object.name
        messages.success(self.request, message_to_send)
        return message
'''
def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {'course':  course}
    if request.method == "POST":
        message = "Course %s has been deleted." % course.name
        course.delete()
        messages.success(request, message)
        return redirect('index')
    return render(request, 'courses/remove.html', context)
'''

def add_lesson(request, course_id):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            message = 'Lesson %s has been successfully added.' % form['subject'].value()
            messages.success(request, message)
            return redirect('courses:detail', course_id=course_id)
    else:
        form = LessonModelForm(initial={'course': course_id})
    context = {'form': form}
    return render(request, 'courses/add_lesson.html', context)