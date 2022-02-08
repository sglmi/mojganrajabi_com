from django.shortcuts import render
from django.views.generic import ListView

from course.models import Course


def index(request):
    return render(request, "home/index.html")


class HomeView(ListView):
    models = Course
    context_object_name = "courses"
    template_name = "home/index.html"
    queryset = Course.objects.all()
