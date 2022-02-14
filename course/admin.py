from csv import list_dialects
from django.contrib import admin


from .models import Course, Chapter, Lesson


class ChapterInline(admin.TabularInline):
    model = Chapter


class LessonInline(admin.TabularInline):
    model = Lesson


class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "date_published", "chapters", "lessons")
    inlines = [
        ChapterInline,
    ]

    def chapters(self, obj):
        chapters = len(obj.chapter_set.all())
        return chapters

    def lessons(self, obj):
        chapters = obj.chapter_set.all()
        lessons = sum(len(chapter.lesson_set.all()) for chapter in chapters)
        return lessons


class ChapterAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "lessons")
    inlines = [
        LessonInline,
    ]

    def lessons(self, obj):
        lessons = len(obj.lesson_set.all())
        return lessons


class LessonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Lesson, LessonAdmin)
