# Generated by Django 2.2.1 on 2020-05-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='price',
            field=models.IntegerField(),
        ),
    ]
