# Generated by Django 3.0.6 on 2020-05-24 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='cheading0',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='cheading1',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='cheading2',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
