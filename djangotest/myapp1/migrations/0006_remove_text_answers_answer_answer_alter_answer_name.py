# Generated by Django 4.1.5 on 2023-02-19 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0005_remove_answer_text_text_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='answers',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='answer',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
