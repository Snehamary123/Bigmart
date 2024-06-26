# Generated by Django 5.0.4 on 2024-05-30 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_registerdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registerdb',
            old_name='name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='registerdb',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='registerationpics'),
        ),
        migrations.AlterField(
            model_name='registerdb',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
