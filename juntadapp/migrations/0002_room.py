# Generated by Django 4.1.4 on 2023-01-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juntadapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleRoom', models.CharField(max_length=50)),
                ('passwordRoom', models.CharField(max_length=50)),
            ],
        ),
    ]
