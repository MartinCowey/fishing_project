# Generated by Django 4.2.16 on 2024-12-04 14:56

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfFish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfFishing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('profile_pic', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('favourite_fish', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.typeoffish')),
                ('favourite_fishing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.typeoffishing')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
