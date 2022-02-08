from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=512)
    discription = models.TextField()

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=512)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    video = models.FileField(upload_to="videos")
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.chapter.name
