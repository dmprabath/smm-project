# Generated by Django 2.2.1 on 2020-05-21 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotation',
            old_name='package',
            new_name='packNo',
        ),
    ]
