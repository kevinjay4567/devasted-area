# Generated by Django 4.2.7 on 2023-11-27 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clima',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ubicacion', models.CharField(max_length=150)),
                ('temperatura', models.FloatField()),
                ('precipitacion', models.CharField(max_length=50)),
                ('viento', models.FloatField()),
                ('resumen', models.CharField(max_length=150)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
        ),
    ]
