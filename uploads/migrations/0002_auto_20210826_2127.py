# Generated by Django 3.2.6 on 2021-08-26 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set_intensity',
            name='max_inten',
            field=models.FloatField(default=99),
        ),
        migrations.AlterField(
            model_name='set_intensity',
            name='min_inten',
            field=models.FloatField(default=1),
        ),
    ]