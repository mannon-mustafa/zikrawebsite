# Generated by Django 4.1.4 on 2023-11-01 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0003_performance_fee_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='conduct',
            field=models.CharField(max_length=300),
        ),
    ]