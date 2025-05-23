# Generated by Django 5.1.7 on 2025-05-17 06:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_image_image_alter_image_created_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
