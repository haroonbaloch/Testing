# Generated by Django 2.1.1 on 2018-09-29 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptwo', '0004_auto_20180929_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='field1',
            field=models.CharField(max_length=264),
        ),
    ]
