from django.contrib import admin


from .models import Course, Chapter, Lesson


class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "date_published", "chapters", "lessons")

    def chapters(self, obj):
        chapters = len(obj.chapter_set.all())
        return chapters

    def lessons(self, obj):
        chapters = obj.chapter_set.all()
        lessons = sum(len(chapter.lesson_set.all()) for chapter in chapters)
        return lessons


admin.site.register(Course, CourseAdmin)


admin.site.register(Chapter)
admin.site.register(Lesson)
