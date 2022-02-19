from multiprocessing import context
from django.shortcuts import render
from course.models import Course


def buy(request, course_pk):
    course = Course.objects.get(pk=course_pk)
    bank_account = "1234-9876-8778-00998"
    email = "mojgan.rajabi@gmail.com"
    return render(
        request,
        "payment/buy.html",
        {"course": course, "bank_account": bank_account, "email": email},
    )
