from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


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
    # users = models.ManyToManyField(User)
    link = models.CharField(max_length=255, default="somelink.com/course")

    def get_absolute_url(self):
        return reverse("course-detail", kwargs={"pk": self.pk})

    def lessons(self):
        return [
            lesson
            for chapter in self.chapter_set.all()
            for lesson in chapter.lesson_set.all()
        ]

    def number_of_lessons(self):
        return len(self.lessons())

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

    # list of users bought the course of the lesson.
    def users(self):
        pass

    def get_absolute_url(self):
        return reverse("lesson-detail", kwargs={"pk": self.pk})

    def course(self):
        return self.chapter.course

    def __str__(self):
        return self.title
