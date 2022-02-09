from django.db import models
from django.urls import reverse
from django.utils import timezone


class Course(models.Model):
    image = models.ImageField(upload_to="images/course", default="course_defualt.jpg")
    title = models.CharField(max_length=127)
    subtitle = models.CharField(max_length=255)
    detail = models.TextField()
    date_published = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("course-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=256)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    video = models.FileField(upload_to="videos")
    title = models.CharField(max_length=128)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
