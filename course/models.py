from email.policy import default
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Course(models.Model):
    PAYMENT_STATUS = (
        ("free", "Free"),
        ("paid", "Paid"),
    )
    image = models.ImageField(upload_to="images/courses", default="course.jpg")
    promotion = models.FileField(upload_to="videos/courses/")
    title = models.CharField(max_length=127)
    subtitle = models.CharField(max_length=255)
    detail = models.TextField()
    date_published = models.DateField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=99.99)
    payment_status = models.CharField(
        max_length=4, choices=PAYMENT_STATUS, default="paid"
    )

    def get_absolute_url(self):
        return reverse("course-detail", kwargs={"pk": self.pk})

    def number_of_lessons(self):
        return sum(len(chapter.lesson_set.all()) for chapter in self.chapter_set.all())

    def __str__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=256)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    PAYMENT_STATUS = (
        ("free", "Free"),
        ("paid", "Paid"),
    )
    video = models.FileField(upload_to=f"videos/lessons/")
    title = models.CharField(max_length=128)
    payment_status = models.CharField(
        max_length=4, choices=PAYMENT_STATUS, default="paid"
    )
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("lesson-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
