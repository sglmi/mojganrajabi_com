from django.urls import path

from . import views

urlpatterns = [
    path("buy/<int:course_pk>/", views.buy, name="buy"),
]
