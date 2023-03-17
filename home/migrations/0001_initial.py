# Generated by Django 4.1.6 on 2023-02-15 13:40

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField(blank=True)),
                ('rank', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('slug', models.CharField(max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=500, unique=True)),
                ('icon', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('post', models.CharField(max_length=400)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=400)),
                ('username', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=200)),
                ('star', models.IntegerField(default=1)),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('rank', models.IntegerField(null=True)),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=500, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=500, unique=True)),
                ('price', models.IntegerField()),
                ('discounted_price', models.IntegerField()),
                ('image', models.ImageField(upload_to='media')),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('specification', ckeditor.fields.RichTextField(blank=True)),
                ('stock', models.CharField(choices=[('in', 'In Stock'), ('out', 'Out of Stock')], max_length=100)),
                ('labels', models.CharField(blank=True, choices=[('new', 'new'), ('hot', 'hot'), ('sale', 'sale'), ('', 'default')], max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300, unique=True)),
                ('checkout', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]
