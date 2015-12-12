from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from courses.models import Course, Lesson
from pybursa.views import MixinTitle


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=self.get_object().id)
        return context


# def detail(request, course_id):
#     courses = Course.objects.get(id=course_id)
#     lessons = courses.lesson_set.all()
#     coaches = courses.coach.user.get_full_name()
#     assistants = courses.assistant.user.get_full_name()
#     return render(request,
#                   'courses/detail.html', {
#                       'courses': courses,
#                       'lessons': lessons,
#                       'coaches': coaches,
#                       'assistants': assistants
#                   })

class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/add.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        messages.success(
            self.request, 'Course %s has been successfully added.' % (data['name']))
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        messages.success(
            self.request, 'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('courses:edit', args=(self.object.pk,))


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    context_object_name = 'course'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Course deletion"
        return context

    def delete(self, request, *args, **kwargs):
        message = super(CourseDeleteView, self).delete(
            request, *args, **kwargs)
        messages.success(self.request, 'Course %s has been deleted.' % (
            self.object.name))
        return message


class LessonCreateView(MixinTitle, CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'
    title = 'Create Lesson'

    # success_url = reverse_lazy('courses:detail')

    def form_valid(self, form):
        data = form.cleaned_data
        messages.success(
            self.request, 'Lesson %s has been successfully added.' % (data['subject']))
        return super(LessonCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.object.get_url()

        # context_object_name = 'lesson'

    # def add_lesson(request, pk):
    #     course = Course.objects.get(id=pk)
    #     if request.POST:
    #         form = LessonModelForm(request.POST)
    #         if form.is_valid():
    #             data = form.cleaned_data
    #             form.save()
    #             messages.success(request, 'Lesson %s has been successfully added.' % (
    #                 data['subject']))
    #             return redirect('courses:detail', data['course'].id)
    #     else:
    #         form = LessonModelForm(initial={'course': pk})
    #     return render(request, 'courses/add_lesson.html', {'form': form})

    # model = Student
    # success_url = reverse_lazy('students:list_view')

    # def get_context_data(self, **kwargs):
    #     data = super(StudentDeleteView, self).get_context_data(**kwargs)
    #     data['title'] = 'Student info suppression'
    #     return data

    # def delete(self, request, *args, **kwargs):
    #     message = super(StudentDeleteView, self).delete(
    #         request, *args, **kwargs)
    #     messages.success(self.request, 'Info on %s %s has been sucessfully deleted.' % (
    #         self.object.name, self.object.surname))
    #     return message

# def add(request):
#     context = {}
#     if request.POST:
#         form = CourseModelForm(request.POST)
#         if form.is_valid():
#             course = form.cleaned_data
#             form.save()
#             messages.success(
#                 request, 'Course %s has been successfully added.' % course['name'])
#             return redirect('index')
#     else:
#         context['form'] = CourseModelForm()
#     # context['form'] = form
#     return render(request, 'courses/add.html', context)


# def edit(request, pk):
#     context = {}
#     course = Course.objects.get(id=pk)
#     if request.method == 'POST':
#         form = CourseModelForm(request.POST, instance=course)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'The changes have been saved.')
#             return redirect('courses:edit', pk)
#     else:
#         context['form'] = CourseModelForm(instance=course)
#     return render(request, 'courses/edit.html', context)


# def remove(request, pk):
#     course = Course.objects.get(id=pk)
#     if request.method == "POST":
#         course.delete()
#         messages.success(request, 'Course %s has been deleted.' % (
#             course.name))
#         return redirect('index')
#     return render(request, 'courses/remove.html', {'course': course})


# def add_lesson(request, pk):
#     course = Course.objects.get(id=pk)
#     if request.POST:
#         form = LessonModelForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             form.save()
#             messages.success(request, 'Lesson %s has been successfully added.' % (
#                 data['subject']))
#             return redirect('courses:detail', data['course'].id)
#     else:
#         form = LessonModelForm(initial={'course': pk})
#     return render(request, 'courses/add_lesson.html', {'form': form})
