# Generated by Django 5.0.4 on 2024-05-06 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorydb',
            old_name='categoryimg',
            new_name='category_img',
        ),
        migrations.RenameField(
            model_name='categorydb',
            old_name='name',
            new_name='category_name',
        ),
    ]
