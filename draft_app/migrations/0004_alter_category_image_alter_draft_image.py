# Generated by Django 4.0 on 2022-06-07 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft_app', '0003_alter_draft_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category_images'),
        ),
        migrations.AlterField(
            model_name='draft',
            name='image',
            field=models.ImageField(upload_to='draft_images'),
        ),
    ]