# Generated by Django 4.1.9 on 2023-05-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacations',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('reason', models.TextField(max_length=255)),
            ],
        ),
    ]