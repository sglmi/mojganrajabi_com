# Generated by Django 4.0.3 on 2022-03-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_course_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='users',
        ),
        migrations.AddField(
            model_name='course',
            name='link',
            field=models.CharField(default='somelink.com/course', max_length=255),
        ),
    ]
