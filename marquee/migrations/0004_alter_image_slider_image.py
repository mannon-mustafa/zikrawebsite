# Generated by Django 4.1.4 on 2023-04-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marquee', '0003_image_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_slider',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
