from django.urls import path


from .views import course_list
from .views import CourseDetailView

urlpatterns = [
    path("", course_list, name="course-list"),
    path("<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
]
