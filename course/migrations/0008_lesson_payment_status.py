# Generated by Django 4.0.2 on 2022-02-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_rename_name_chapter_title_lesson_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='payment_status',
            field=models.CharField(choices=[('free', 'Free'), ('paid', 'Paid')], default='paid', max_length=4),
            preserve_default=False,
        ),
    ]