from django.urls import path


from .views import ChapterDetailView
from .views import CourseDetailView, CourseListView

urlpatterns = [
    path("", CourseListView.as_view(), name="course-list"),
    path("<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
    path("lessons/<int:pk>/", ChapterDetailView.as_view(), name="lesson-detail"),
]
