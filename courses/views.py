import logging
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages

from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

logger = logging.getLogger(__name__)


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course_detail'
    template_name = 'courses/detail.html'
    logger.debug("Courses detail view has been debugged")
    logger.info("Logger of courses detail view informs you!")
    logger.warning("Logger of courses detail view warns you!")
    logger.error("Courses detail view went wrong!")

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons_list'] = Lesson.objects.filter(course=self.object.id) 
        return context

class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, "Course %s has been successfully added." % form.cleaned_data['name'])
        return super(CourseCreateView, self).form_valid(form)  

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'courses/edit.html'   

    def form_valid(self, form):
        messages.success(self.request, "The changes have been saved.")
        self.success_url = reverse('courses:edit', args=(form.instance.id,))
        return super(CourseUpdateView, self).form_valid(form)  

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html' 

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        messages.success(self.request, "Course %s has been deleted." % course.name)
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

def add_lesson(request, course_id):
    cd = Course.objects.get(id=course_id)
    if request.POST:
        form = LessonModelForm(request.POST)
        if form.is_valid():
            form.save()
            text = "Lesson " + form.cleaned_data['subject'] + " has been successfully added."
            messages.success(request, text)
            return redirect('courses:detail',course_id)
    else:
        form = LessonModelForm(initial={'course':course_id})
        form.fields['course'].queryset = Course.objects.all()
    return render(request, 'courses/add_lesson.html', {'form': form})
