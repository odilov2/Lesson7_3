# Generated by Django 5.0.4 on 2024-05-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albom',
            name='cover',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='songs',
            name='cover',
            field=models.URLField(null=True),
        ),
    ]
