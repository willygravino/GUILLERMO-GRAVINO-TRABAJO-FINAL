# Generated by Django 4.1.7 on 2023-03-24 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminVideos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='quienes_aparecen',
            field=models.CharField(max_length=120, verbose_name='Ingrese el nombre y apellido de quienes participan en el video, separados por coma'),
        ),
    ]
