from django.shortcuts import render
from django.views.generic import DetailView
from .models import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, "course/courses.html", {"courses": courses})


class CourseDetailView(DetailView):
    model = Course
    template_name = "course/course_detail.html"
    context_object_name = "course"
