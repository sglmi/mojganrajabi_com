from django.urls import path


from .views import ChapterDetailView, course_list
from .views import CourseDetailView

urlpatterns = [
    path("", course_list, name="course-list"),
    path("course/<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
    path("lessons/<int:pk>/", ChapterDetailView.as_view(), name="lesson-detail"),
]
