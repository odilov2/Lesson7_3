# Generated by Django 5.0.4 on 2024-05-14 16:16

import django.db.models.deletion
import mdeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FeaturedProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', mdeditor.fields.MDTextField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='product/product')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', mdeditor.fields.MDTextField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='product/product')),
                ('country', models.CharField(max_length=20)),
                ('lifetime', models.DateField()),
                ('quality', models.CharField(max_length=30)),
                ('checks', models.CharField(max_length=20)),
                ('weight', models.FloatField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categories')),
            ],
        ),
    ]