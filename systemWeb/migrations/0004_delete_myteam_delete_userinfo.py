# Generated by Django 4.2.7 on 2023-11-09 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systemWeb', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyTeam',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
