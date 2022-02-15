from django.shortcuts import render
from django.views.generic import DetailView

from .models import Chapter, Course, Lesson


def course_list(request):
    courses = Course.objects.all()
    return render(request, "course/courses.html", {"courses": courses})


class CourseDetailView(DetailView):
    model = Course
    template_name = "course/course_detail.html"
    context_object_name = "course"


class ChapterDetailView(DetailView):
    model = Chapter
    template_name = "course/chapter_detail.html"
    context_object_name = "chapter"


class ChapterDetailView(DetailView):
    model = Lesson
    template_name = "course/lesson_detail.html"
    context_object_name = "lesson"
