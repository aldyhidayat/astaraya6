# Generated by Django 2.2.12 on 2020-12-26 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20201226_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image2',
        ),
    ]
