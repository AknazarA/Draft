# Generated by Django 4.0 on 2022-06-19 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft_app', '0012_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.SlugField(max_length=15),
        ),
    ]
