# Generated by Django 5.0.4 on 2024-05-29 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_productdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerationdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('profilepic', models.ImageField(blank=True, null=True, upload_to='profilepics')),
            ],
        ),
    ]