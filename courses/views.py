from django.shortcuts import redirect, render
#from django.http import HttpResponse
from django.views import generic
from courses.models import Course, Lesson
from coaches.models import Coach
from courses import forms
from django.contrib import messages


# Create your views here.
#def index_courses(request):
    #courses_list = Course.objects.all()
    #context = {'courses_list': courses_list}
    #return render(request, 'index.html', context)
    #return render(request, 'index.html', {'courses_list': Course.objects.all()})

class DetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the related Lessons
        #context['lessons_list'] = Lesson.objects.all()
        #Lessons filtered by course_id received in URL
        context['lessons_list'] = Lesson.objects.filter(course_id=self.kwargs.get(self.pk_url_kwarg, None))
        ##context['lessons_list'] = Lesson.objects.filter(course_id=self.kwargs['pk'])
        #Coaches filtered by course_id received in URL
        #context['coaches_list'] = Coach.objects.all()
        context['coaches_list'] = Coach.objects.filter(coach_courses=self.kwargs.get(self.pk_url_kwarg, None))
        ##context['coaches_list'] = Coach.objects.filter(coach_courses=self.kwargs['pk'])
        context['assistants_list'] = Coach.objects.filter(assistant_courses=self.kwargs.get(self.pk_url_kwarg, None))
        ##context['assistant_list'] = Coach.objects.filter(assistant_courses=self.kwargs['pk'])
        return context


def add(request):
    if request.method == 'POST':
        form = forms.CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Course %s has been successfully added.' % course.name)
            return redirect('/')
    else:
        form = forms.CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})


def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', pk)
    else:
        form = forms.CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course %s has been deleted.' % course.name)
        return redirect('/')
    return render(request, 'courses/remove.html', {'course': course})
