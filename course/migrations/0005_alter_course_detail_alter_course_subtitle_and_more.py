# Generated by Django 4.0.2 on 2022-02-09 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_rename_description_course_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='subtitle',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
