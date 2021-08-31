# Generated by Django 3.2.6 on 2021-08-27 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('title', models.CharField(max_length=200)),
                ('action', models.CharField(choices=[('tif file', 'tif'), ('no tif file', 'no_tif')], max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('min_inten', models.FloatField(default=1)),
                ('max_inten', models.FloatField(default=99)),
            ],
        ),
    ]
