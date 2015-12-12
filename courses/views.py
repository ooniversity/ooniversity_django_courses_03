<<<<<<< HEAD
<<<<<<< HEAD
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
=======
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
>>>>>>> 1ebe173911795743f7ef0495cc1b0aa19c8b3fa2


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course_detail'
    template_name = 'courses/detail.html'

<<<<<<< HEAD
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
=======
def add(request):
    if request.POST:
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            text = "Course " + form.cleaned_data['name'] + " has been successfully added."
            messages.success(request, text)
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})
=======
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course_detail'
    template_name = 'courses/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons_list'] = Lesson.objects.filter(course=self.object.id) 
        return context
>>>>>>> 4cbe27320e7ae78f3c102275fc2f9f1fb4d19c11

class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')

<<<<<<< HEAD
def remove(request, course_id):
    cd = Course.objects.get(id=course_id)
    if request.method == "POST":
        text = "Course " + cd.name + " has been deleted."
        messages.success(request, text)  
        cd.delete()
        return redirect('index')
    return render(request, 'courses/remove.html', {'cd': cd})    
>>>>>>> 1ebe173911795743f7ef0495cc1b0aa19c8b3fa2
=======
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
>>>>>>> 4cbe27320e7ae78f3c102275fc2f9f1fb4d19c11

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