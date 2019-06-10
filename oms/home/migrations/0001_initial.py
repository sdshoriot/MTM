# Generated by Django 2.1.4 on 2019-01-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='author_images')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arabic_since', models.CharField(blank=True, max_length=100, null=True)),
                ('arabic_name', models.CharField(blank=True, max_length=100, null=True)),
                ('arabic_history', models.TextField()),
                ('mtm_since', models.CharField(blank=True, max_length=100, null=True)),
                ('mtm_name', models.CharField(blank=True, max_length=200, null=True)),
                ('mtm_meaning', models.CharField(blank=True, max_length=200, null=True)),
                ('mtm_history', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]