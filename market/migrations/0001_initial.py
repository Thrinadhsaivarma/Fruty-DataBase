# Generated by Django 4.2.13 on 2024-05-20 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=100)),
                ('Scientific_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='images')),
                ('season_name', models.CharField(max_length=100)),
                ('cost', models.CharField(max_length=100)),
            ],
        ),
    ]
