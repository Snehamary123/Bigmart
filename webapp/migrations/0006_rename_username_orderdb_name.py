# Generated by Django 5.0.4 on 2024-06-11 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_orderdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdb',
            old_name='username',
            new_name='Name',
        ),
    ]
