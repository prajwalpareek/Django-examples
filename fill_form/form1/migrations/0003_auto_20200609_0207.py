# Generated by Django 3.0.3 on 2020-06-08 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0002_auto_20200609_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
