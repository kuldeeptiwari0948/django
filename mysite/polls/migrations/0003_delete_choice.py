# Generated by Django 4.2.6 on 2023-10-29 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_choice_choice_text_remove_choice_question_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
