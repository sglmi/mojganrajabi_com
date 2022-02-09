# Generated by Django 4.0.2 on 2022-02-09 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_course_date_published_alter_course_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='lesson',
            name='title',
            field=models.CharField(default='hello', max_length=128),
            preserve_default=False,
        ),
    ]
