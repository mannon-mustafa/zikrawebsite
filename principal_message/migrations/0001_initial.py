# Generated by Django 4.1.4 on 2024-02-21 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='principal_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(null=True, upload_to='video/%y')),
                ('caption', models.CharField(max_length=600)),
            ],
        ),
    ]
