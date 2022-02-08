from django.db import models
from django.urls import reverse


class Course(models.Model):
    image = models.ImageField(upload_to="images/course", default="course_defualt.jpg")
    title = models.CharField(max_length=256)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("course-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=256)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    video = models.FileField(upload_to="videos")
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.chapter.name
