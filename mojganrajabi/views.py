from django.shortcuts import render
from django.views.generic import ListView

from course.models import Course
from blog.models import About


def index(request):
    return render(request, "home/index.html")


class HomeView(ListView):
    models = Course
    context_object_name = "courses"
    template_name = "home/index.html"
    queryset = Course.objects.all()


class AboutView(ListView):
    model = About
    template_name = "home/about.html"
