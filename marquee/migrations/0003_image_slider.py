# Generated by Django 4.1.4 on 2023-04-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marquee', '0002_notice_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='image_slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]