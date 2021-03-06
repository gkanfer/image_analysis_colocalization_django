# Generated by Django 3.2.6 on 2021-09-01 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_2', models.ImageField(upload_to='images')),
                ('title_2', models.CharField(default='Ch2', max_length=200)),
                ('min_inten_2', models.FloatField(default=1)),
                ('max_inten_2', models.FloatField(default=76)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('title', models.CharField(default='Ch1', max_length=200)),
                ('min_inten', models.FloatField(default=1)),
                ('max_inten', models.FloatField(default=76)),
            ],
        ),
    ]
