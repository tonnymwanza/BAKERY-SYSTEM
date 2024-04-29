# Generated by Django 3.2.7 on 2024-04-25 17:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bakery_app', '0003_auto_20240425_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribing',
            name='subscribe',
            field=models.ManyToManyField(null=True, related_name='subscriber', to=settings.AUTH_USER_MODEL),
        ),
    ]