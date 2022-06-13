# Generated by Django 4.0 on 2022-06-09 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft_app', '0005_draft_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='draft',
            name='category',
        ),
        migrations.AddField(
            model_name='draft',
            name='category',
            field=models.ManyToManyField(to='draft_app.Category'),
        ),
    ]
