# Generated by Django 5.0 on 2023-12-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('Planet', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='projects', verbose_name='Imagen')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Enlace')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
    ]