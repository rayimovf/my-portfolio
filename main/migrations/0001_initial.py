# Generated by Django 5.0 on 2024-05-10 04:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='about_me_img')),
                ('title', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('position', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=75)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('birthday', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('title', models.CharField(max_length=75)),
                ('date', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo')),
                ('name', models.CharField(max_length=100)),
                ('video', models.URLField(blank=True, null=True)),
                ('email_one', models.EmailField(max_length=254)),
                ('email_two', models.EmailField(max_length=254)),
                ('facebook', models.URLField()),
                ('address', models.CharField(max_length=100)),
                ('phone_number_one', models.CharField(max_length=20)),
                ('phone_number_two', models.CharField(max_length=20)),
                ('instagram', models.URLField()),
                ('telegram', models.URLField()),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news_img')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio_img')),
                ('name', models.CharField(max_length=75)),
                ('service', models.CharField(max_length=75)),
                ('banner', models.ImageField(upload_to='portfolio_banner')),
                ('client', models.CharField(max_length=100)),
                ('project_type', models.CharField(max_length=75)),
                ('date', models.DateField()),
                ('about', models.TextField()),
                ('github_link', models.URLField(blank=True, null=True)),
                ('figma_link', models.URLField(blank=True, null=True)),
                ('website_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='services_icon')),
                ('title', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('percent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MyHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='my_photo')),
                ('position', models.ManyToManyField(to='main.position')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.biography')),
                ('education', models.ManyToManyField(to='main.education')),
                ('skills', models.ManyToManyField(to='main.skills')),
            ],
        ),
    ]
