# Generated by Django 4.1.4 on 2023-05-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='rollno',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
