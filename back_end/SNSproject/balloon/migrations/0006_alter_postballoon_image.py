# Generated by Django 3.2.9 on 2022-03-22 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balloon', '0005_alter_postballoon_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postballoon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/rest_framework/img/'),
        ),
    ]