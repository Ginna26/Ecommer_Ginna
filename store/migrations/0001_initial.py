# Generated by Django 4.1.1 on 2022-09-29 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=12)),
                ('fecha_n', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('genero', models.CharField(max_length=15)),
            ],
        ),
    ]