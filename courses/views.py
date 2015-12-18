# -*- coding: utf-8 -*- 
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from courses.forms import CourseModelForm, LessonModelForm
from courses.models import Course, Lesson
from pybursa.utils import MixinLessonContext
import logging

logger = logging.getLogger(__name__)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'courses'
    
    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        logger.debug("Courses detail view has been debugged")
        logger.info("Logger of courses detail view informs you!")
        logger.warning("Logger of courses detail view warns you!")
        logger.error("Courses detail view went wrong!")
        context['lessons'] = Lesson.objects.filter(course = self.object)
        return context
    

class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    form_class = CourseModelForm
    context_object_name = 'form'
    success_url = reverse_lazy('index')
    #success_message = u"Course %(name)s has been successfully added."
    
    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context 

    def form_valid(self, form):
        course = form.save()
        messages.success(self.request, u"Course %s has been successfully added." % (course.name))
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    form_class = CourseModelForm
    context_object_name = 'form'
    success_message = u"The changes have been saved."

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context 
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('courses:edit', args = (self.object.pk,))

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
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
        success_message = u"Course {} has been deleted.".format(self.object.name)
        messages.success(self.request, success_message)
        return message


class LessonCreateView(MixinLessonContext, CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'
    form_class = LessonModelForm
    context_object_name = 'form'
    #success_message = u"Lesson %(subject)s has been successfully added."

    def get_initial(self):
        return {'course': self.kwargs['pk']}
    
    #def get_success_url(self, **kwargs):
        #return reverse_lazy('courses:detail', kwargs={'pk': self.object.course_id})

    def form_valid(self, form):
        lesson = form.save()
        messages.success(self.request, u"Lesson %s has been successfully added." % lesson.subject)
        return super(LessonCreateView, self).form_valid(form)


''' 
def detail(request, courses_id):
    try:
        courses = get_object_or_404(Course, pk=courses_id)
        lessons = courses.lesson_set.all()
        return render(request, 'courses/detail.html', { 
                      'courses':courses , 
                      'lessons':lessons,
                      })
    except ObjectDoesNotExist:
        achtung = "Houston, we have a problem with id = {0} exist yet.".format(courses_id) 
	return render(request, 'courses/detail.html', {
		    "achtung": achtung,
            })

  
def add(request):
    if request.method == 'POST':
        course_form = CourseModelForm(request.POST)
        if course_form.is_valid():
            course = course_form.save()
            messages.success(request, u"Course %s has been successfully added." % (course.name))
            return redirect('index')
    else:
        course_form = CourseModelForm()
    return render(request, 'courses/add.html', {
                  'course_form': course_form,
                  })


def edit(request, courses_id):
    course = Course.objects.get(id=courses_id)
    if request.method == 'POST':
        course_form = CourseModelForm(request.POST, instance=course)
        if course_form.is_valid():
            course = course_form.save()
            messages.success(request, "The changes have been saved.")
            return redirect('courses:edit', courses_id)
    else:
        course_form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {
                  'course_form': course_form,
                  })
    


def remove(request, courses_id): 
    course_remove = Course.objects.get(id=courses_id)
    remove_massage = u"Вы уверены, что хотите удалить информацию о %s ?" % (course_remove.name)
    if request.method == 'POST':
        course_remove.delete()
        messages.success(request, u"Course %s has been deleted." % (course_remove.name))
        return redirect('index')
    return render(request, 'courses/remove.html',{
                  'remove_massage': remove_massage,
                  })


def add_lesson(request, courses_id):
    if request.method == 'POST':
        lesson_form = LessonModelForm(request.POST)
        if lesson_form.is_valid():
            lessons = lesson_form.save()
            messages.success(request, u"Lesson %s has been successfully added." % (lessons.subject))
            return redirect('courses:detail', courses_id)
    else:
        lesson_form = LessonModelForm()
    return render(request, 'courses/add_lesson.html', {
                  'lesson_form': lesson_form,
                  })
'''


         
