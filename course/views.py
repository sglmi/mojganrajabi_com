from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Chapter, Course, Lesson


class CourseAccessMixin(UserPassesTestMixin):
    def test_func(self):
        user = User.objects.get(username=self.request.user.username)
        print(dir(user))
        url_list = [item for item in self.request.get_full_path().split("/") if item]
        course_id = url_list[-1]
        course = Course.objects.get(pk=course_id)
        print(dir(course.users))
        usernames = [user.username for user in course.users.all()]
        return self.request.user.username in usernames


class CourseListView(ListView):
    model = Course
    template_name = "course/courses.html"
    context_object_name = "courses"


class CourseDetailView(LoginRequiredMixin, CourseAccessMixin, DetailView):
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
