# Generated by Django 3.2.9 on 2021-12-29 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGestion', '0011_auto_20211230_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faire_stage',
            name='NivEtude',
            field=models.IntegerField(choices=[(1, 'CP1'), (3, 'CS1'), (5, 'CS3')]),
        ),
    ]
