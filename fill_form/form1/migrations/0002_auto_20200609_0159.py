# Generated by Django 3.0.3 on 2020-06-08 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='number',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
