# Generated by Django 4.0 on 2022-06-19 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft_app', '0008_post_alter_category_image_alter_termin_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageblock',
            name='image',
            field=models.ImageField(default='', upload_to='image_block_images'),
            preserve_default=False,
        ),
    ]