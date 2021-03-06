# Generated by Django 3.0.2 on 2020-02-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['car_name']},
        ),
        migrations.AddField(
            model_name='city',
            name='offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='city',
            name='price',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='city',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_rent',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_name',
            field=models.CharField(max_length=40),
        ),
    ]
