# Generated by Django 4.2.1 on 2023-07-08 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='padd',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
