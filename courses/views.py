from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse



class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/detail.html"
    context_object_name = 'course'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        lessons = Lesson.objects.filter(course=self.object)
        context['lessons'] = lessons
        return context

class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'
    context_object_name = 'course'
    template_name = 'courses/add.html'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        messages.success(self.request, 'Course %s has been successfully added.' % (data['name']))
        return super(CourseCreateView, self).form_valid(form)

class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    context_object_name = 'course'
    template_name = 'courses/edit.html'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        messages.success(self.request, 'Info on the course %s has been sucessfully changed.' % (data['name']))
        return super(CourseUpdateView, self).form_valid(form)

class CourseDeleteView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        messages.success(self.request, 'Course %s has been deleted.' % (course.name))
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)

def detail(request,pk):
    coach={}
    assistant={}
    course=Course.objects.get(id=pk)
    coach['fio']=course.coach.user.get_full_name()
    assistant['fio']=course.assistant.user.get_full_name()
    coach['id']=course.coach.id
    assistant['id']=course.assistant.id
    coach['description']=course.coach.description
    assistant['description']=course.assistant.description
    lessons=Lesson.objects.filter(course_id=pk)
    return render(request, 'courses/detail.html', {"lessons": lessons,"course":course,'coach':coach,'assistant':assistant})

def add(request):
    form = CourseModelForm()
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            add_course = form.save()
            messages.success(request, u'Course %s has been successfully added.' % (add_course.name))
            return redirect('index')
    return render(request,'courses/add.html',{'form':form})

def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, u'The changes have been saved.')
            return redirect('courses:edit', pk)
    else:
        form = CourseModelForm(instance=course)
    return render(request,'courses/edit.html',{'form':form})

def remove(request,pk):
    course = Course.objects.get(id=pk)
    message = u"%s" %(course.name)
    if request.method == 'POST':
        course.delete()
        messages.success(request, u"Course %s has been deleted." % (course.name))
        return redirect('index')
    return render(request, 'courses/remove.html', {'message': message})
    
def add_lesson(request,pk):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            add_lesson = form.save()
            messages.success(request, u"Lesson %s has been successfully added." % (add_lesson.subject))
            return redirect('courses:detail', pk)
    else:
        form = LessonModelForm(initial= {'course': pk})
    return render(request,'courses/add_lesson.html',{'form':form})