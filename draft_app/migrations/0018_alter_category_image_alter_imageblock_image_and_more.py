# Generated by Django 4.0 on 2022-07-29 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft_app', '0017_alter_termin_text_alter_termin_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='steasy/category_images'),
        ),
        migrations.AlterField(
            model_name='imageblock',
            name='image',
            field=models.ImageField(upload_to='steasy/image_block_images'),
        ),
        migrations.AlterField(
            model_name='termin',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='steasy/draft_images'),
        ),
    ]
