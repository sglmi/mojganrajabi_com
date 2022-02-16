# Generated by Django 4.0.2 on 2022-02-15 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_course_date_created_course_date_modified_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
        migrations.AddField(
            model_name='course',
            name='promotion',
            field=models.FileField(default=1, upload_to='video/courses/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.FileField(upload_to='videos/lessons/'),
        ),
    ]