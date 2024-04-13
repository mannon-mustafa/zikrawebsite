# Generated by Django 4.1.4 on 2024-03-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_diary_fourth_diary_lkg_diary_nursary_diary_second_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='diary_fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=50)),
                ('rollno', models.IntegerField()),
                ('fee_status', models.BooleanField(default='True')),
            ],
        ),
        migrations.RemoveField(
            model_name='diary_first',
            name='fee_status',
        ),
        migrations.RemoveField(
            model_name='diary_fourth',
            name='fee_status',
        ),
        migrations.RemoveField(
            model_name='diary_lkg',
            name='fee_status',
        ),
        migrations.RemoveField(
            model_name='diary_nursary',
            name='fee_status',
        ),
        migrations.RemoveField(
            model_name='diary_second',
            name='fee_status',
        ),
        migrations.RemoveField(
            model_name='diary_third',
            name='fee_status',
        ),
        migrations.RemoveField(
            model_name='diary_ukg',
            name='fee_status',
        ),
    ]
