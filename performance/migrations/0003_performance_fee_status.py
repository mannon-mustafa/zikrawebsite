# Generated by Django 4.1.4 on 2023-06-19 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0002_performance_rollno'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='fee_status',
            field=models.BooleanField(default='True'),
        ),
    ]
